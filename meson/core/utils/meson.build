utils_inc = include_directories('../../../src/utils/')
m_d = '../../../src/utils/'
inc +=  [utils_inc]

utils_sources = files([
    m_d + 'BufferStore.cc',
    m_d + 'CppPyWrapper.cc',


])

utils_lib = static_library('utils',
    sources: utils_sources,
    include_directories: inc,
#    install: true,
#    link_args: link_a,
)