import sys

from setuptools import Extension, setup
from pathlib import Path
import os
import compile_assist
from compile_assist.libraries import find_library, find_mpi

# main dir is special
# we need it in include but not the actual main.cc
# libmain contains python package def, we don't want it in C++ sources

src = []

for f in Path("src").rglob("*.cc"):
    excludes = ["main/main.cc"]
    include = True
    for e in excludes:
        if str(f).endswith(e):
            include = False
    if include:
        src.append(str(f))

mpi = find_mpi()

if mpi:
    library_dirs, libraries, include_dirs, extra_compile_args = mpi
else:
    library_dirs, libraries, include_dirs, extra_compile_args = [], [], [], ["-DUSE_MPI=0"]
    print('MPI not found will be compiled without MPI support')

fftw = find_library('fftw3', ['/opt/homebrew/'])
if fftw:
    library_dirs += fftw[0]
    libraries += fftw[1]
    include_dirs += fftw[2]
    extra_compile_args += fftw[3]
else:
    print('Stop. Library fftw3 not found')
    sys.exit()


for folder in os.walk("src"):
    excludes = ["src", "src/libmain", "src/libmain/orbit"]
    if folder[0] not in excludes:
        include_dirs.append(folder[0])
        print(folder[0])

extension_mod = Extension(
    "orbit.core._orbit",
    sources=src,
    libraries=libraries,
    include_dirs=include_dirs,
    library_dirs=library_dirs,
    extra_compile_args=extra_compile_args + ["-Wl,--enable-new-dtags"],
    extra_link_args=["-lm", "-fPIC"],
)

packages = ["orbit.core"]
for folder in os.walk("py/orbit"):
    path = os.path.normpath(folder[0])
    path = path.split(os.sep)
    packages.append(".".join(path[1:]))

package_dir = {
    "orbit": "py/orbit",
    "orbit.core": "src/libmain/orbit",
}

# This snippet generates the package structure of the orbit.core modules
# including the __init__.py file for each module
# The purpose is to be able to load individual modules from orbit.core in a
# Pythonic fashion.
core_modules = [
    "aperture",
    "orbit_mpi",
    "trackerrk4",
    "error_base",
    "bunch",
    "teapot_base",
    "linac",
    "spacecharge",
    "orbit_utils",
    "foil",
    "collimator",
    "field_sources",
    "rfcavities",
    "impedances",
    "fieldtracker",
]
for mod in core_modules:
    packages.append(f"orbit.core.{mod}")
    package_dir.update({f"orbit.core.{mod}": "src/libmain/module_template"})


# Define the setup parameters
setup(
    ext_modules=[extension_mod],
    package_dir=package_dir,
    packages=packages,
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    scripts=["bin/pyORBIT"],
)

