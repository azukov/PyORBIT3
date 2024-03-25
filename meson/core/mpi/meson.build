
src = base_src + '/mpi/'
_inc = include_directories(src)
inc += _inc

sources = files([
    src + 'orbit_mpi.cc',
    src + 'wrap_mpi_comm.cc',
    src + 'wrap_mpi_datatype.cc',
    src + 'wrap_mpi_group.cc',
    src + 'wrap_mpi_op.cc',
    src + 'wrap_mpi_request.cc',
    src + 'wrap_mpi_status.cc',
    src + 'wrap_orbit_mpi.cc',
])

lib = library('mpi',
    sources: sources,
    include_directories: inc,
    dependencies : [utils_lib, py3],
    link_args: link_a,
    install: true
)

mpi_lib = declare_dependency(link_with : lib)