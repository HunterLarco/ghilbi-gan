load("@bazel_tools//tools/build_defs/repo:git.bzl", "new_git_repository")
load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "http_zlib",
    build_file = "BUILD.zlib",
    sha256 = "36658cb768a54c1d4dec43c3116c27ed893e88b02ecfcb44f2166f9c0b7f2a0d",
    strip_prefix = "zlib-1.2.8",
    urls = ["https://www.zlib.net/fossils/zlib-1.2.8.tar.gz"],
)

bind(
    name = "zlib",
    actual = "@http_zlib//:zlib",
)

http_archive(
    name = "libpng_http",
    build_file = "BUILD.libpng",
    sha256 = "8b672c7aae42c6c6b06f9f4b6019496669e02df024276a186181bc3365163832",
    strip_prefix = "libpng-1.6.26",
    url = "https://github.com/glennrp/libpng/archive/v1.6.26.tar.gz",
)

bind(
    name = "libpng",
    actual = "@libpng_http//:libpng",
)

new_git_repository(
    name = "opencv",
    remote = "https://github.com/opencv/opencv",
    build_file = "BUILD.opencv",
    tag = "3.1.0",
)
