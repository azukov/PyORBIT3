mpi_inc = include_directories('../../../src/mpi/')
inc += mpi_inc
m_d = '../../../src/mpi/'
mpi_sources = files([
    m_d + 'orbit_mpi.cc',
    m_d + 'wrap_mpi_comm.cc',
    m_d + 'wrap_mpi_datatype.cc',
    m_d + 'wrap_mpi_group.cc',
    m_d + 'wrap_mpi_op.cc',
    m_d + 'wrap_mpi_request.cc',
    m_d + 'wrap_mpi_status.cc',
    m_d + 'wrap_orbit_mpi.cc',
#    m_d + 'wrap_orbit_mpi_comm_functions.cc',
#    m_d + 'wrap_mpi_graph_fucntions.cc',
#    m_d + 'wrap_mpi_group_functions.cc',
#    m_d + 'wrap_mpi_intercom_functions.cc',
#    m_d + 'wrap_mpi_send_receive.cc',

])

mpi_lib = static_library('mpi',
    sources: mpi_sources,
    include_directories: inc,
    dependencies : [utils_d],
#    link_args: link_a,
)