subdir('utils')




subdir('mpi')
#mpi_d = declare_dependency(link_with : mpi_lib)



core_lib = library('core',
#    sources: ['some_file.cc'],
    cpp_args: ['-fPIC', '-std=c++11'],
    dependencies : [utils_lib, mpi_lib],
    install: false,

)

core_dep = declare_dependency(link_with : core_lib)
