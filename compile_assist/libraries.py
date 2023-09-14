import subprocess
import os
from pathlib import Path
from distutils.ccompiler import new_compiler

def parse_options(line):
    library_dirs = []
    libraries = []
    include_dirs = []
    compile_options = []
    for option in line.split(' ')[1:]:
        if option.startswith('-L'):
            library_dirs.append(option[2:])
        elif option.startswith('-l'):
            libraries.append(option[2:])
        elif option.startswith('-I'):
            include_dirs.append(option[2:])
        else:
            compile_options.append(option[2:])

    return library_dirs, libraries, include_dirs, compile_options


def find_mpi(places_to_look=None):
    if not places_to_look:
        places_to_look = []
    for place in places_to_look:
        for p in Path(place).glob('**/mpic++'):
            mpi_compiler = p
            print(f"Found MPI compiler at {mpi_compiler}")
            try:
                result = subprocess.check_output([mpi_compiler, '-showme']).decode().strip()
                options = parse_options(result)
                return options
            except Exception:
                print("MPICC not valid")
    return None

def check_library(name, include_dir=None, lib_dir=None, test_file=None):
    old_path = Path.cwd()
    comp_dir = test_file if test_file else Path(__file__).parent
    os.chdir(comp_dir)

    f_name = f'test_{name}'
    src = f'{f_name}.c'
    obj = f'{f_name}.o'
    try:
        compiler = new_compiler()
        if include_dir:
            compiler.add_include_dir(str(include_dir))
        if lib_dir:
            compiler.add_library_dir(str(lib_dir))
        compiler.add_library(name)
        compiler.compile([src])
        compiler.link_executable([obj], f_name)
        return True
    except Exception as e:
        print(f"Library {name} fails compilation.")
        return False
    finally:
        if Path(f_name).exists():
            os.remove(f_name)
        if Path(obj).exists():
            os.remove(obj)
        os.chdir(old_path)


def find_library(name, places_to_look=None, test_file=None):
    if not places_to_look:
        places_to_look = []
    compiler = new_compiler()
    library = compiler.library_filename(name)

    include_dir = os.getenv(f'{name.upper()}_INCLUDE_DIR', None)
    lib_dir = os.getenv(f'{name.upper()}_LIB_DIR', None)

    if include_dir and lib_dir:
        if check_library(name, include_dir, lib_dir):
            return [lib_dir], [name], [include_dir], []
        else:
            print(f'Environment variable {name.upper()}_INCLUDE_DIR and {name.upper()}_LIB_DIR are set but compilation failed.')
            return None
    elif include_dir or lib_dir:
        print(f'Both environment variables {name.upper()}_INCLUDE_DIR and {name.upper()}_LIB_DIR are required.')
        return None


    env_home = os.getenv(f'{name.upper()}_HOME', None)
    if env_home:
        print(f'Environment variable {name.upper()}_HOME={env_home} found.')
        include_dir, lib_dir = Path(env_home) / 'include',  Path(env_home) / 'lib'
        if check_library(name, include_dir, lib_dir):
            return [lib_dir], [name], [include_dir], []

    print(f'Environment variable {name.upper()}_HOME not found will try existing compiler settings.')

    # Try if all include and lib folders are already set up
    # This will be the case of conda
    if check_library(name):
        return [], [name], [], []
    else:
        print(f'Library {name} is not in current environment.')

    for place in places_to_look:
        for p in Path(place).glob(f'**/{library}'):
            lib_dir = p.parent
            include_dir = lib_dir.parent / 'include'
            if not include_dir.exists():
                continue
            print(f"Found {name} library at {p}")
            if check_library(name, include_dir, lib_dir):
                return [str(lib_dir)], [name], [str(include_dir)], []

    return None






