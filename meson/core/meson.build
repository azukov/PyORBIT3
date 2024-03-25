#py3 = dependency('python3')

subdir('utils')
subdir('mpi')

core_lib = library('core',
#    sources: ['some_file.cc'],
    cpp_args: ['-fPIC', '-std=c++11'],
    dependencies : [utils_lib, mpi_lib, py3],
    install: false,

)

core_dep = declare_dependency(link_with : core_lib)
