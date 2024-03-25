project('orbit', ['cpp'], version: '0.0.1')


# Add Python installation details
python = import('python').find_installation(pure: false)

# Add C++ compiler details
cpp = meson.get_compiler('cpp')

base = meson.current_source_dir() + '/core'
base_src ='../../../src'


inc = ['/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/Headers']
link_a = ['-L/Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.9/lib',
  '-lpython3.9'
]


subdir('core')



# Create the orbit.core.orbit_mpi extension module
mpi_ext = python.extension_module('orbit_mpi',
      sources: [base + '/mpi_init.cc'],
      include_directories: inc,
      cpp_args: ['-fPIC', '-std=c++11'],
      dependencies: [mpi_lib, utils_lib],
      install: true,
      subdir: 'orbit/core',
      link_args: link_a,
)


## Add Python source files (for the linac submodule)
#py_sources = files(['../py/orbit/aperture/__init__.py'])
#
## Create the Python submodule (linac)
#linac_mod = python.install_sources(
#    py_sources,
#    subdir: 'orbit',
#    # pure: true,
#)

