
src = base_src + '/utils/'
_inc = include_directories(src)
inc += _inc

sources = files([
    src + 'BufferStore.cc',
    src + 'CppPyWrapper.cc',
])

lib = library('utils',
    sources: sources,
    include_directories: inc,
    link_args: link_a,
    install: true,
)

utils_lib = declare_dependency(link_with : lib)