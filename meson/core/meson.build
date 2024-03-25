subdir('utils')
utils_d = declare_dependency(link_with : utils_lib)

subdir('mpi')
mpi_d = declare_dependency(link_with : mpi_lib)



core_lib = library('core',
#    sources: ['some_file.cc'],
    cpp_args: ['-fPIC', '-std=c++11'],
    dependencies : [utils_d, mpi_d],
    install: true,
)

core_d = declare_dependency(link_with : core_lib)
