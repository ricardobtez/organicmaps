from conan import ConanFile
from conan.tools.cmake import cmake_layout
from conan.errors import ConanInvalidConfiguration


class OrganicMapsDeps(ConanFile):
    name = "organicmaps-deps"
    version = "1.0.0"
    description = "Conan-managed system dependencies for the Organic Maps desktop build (WITH_SYSTEM_PROVIDED_3PARTY)"
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps", "CMakeToolchain"
    options = {
        "with_tests": [True, False],
    }
    default_options = {
        "with_tests": False,
        "boost/*:header_only": True,
        "gtest/*:shared": False,
        "harfbuzz/*:with_icu": True,
        "harfbuzz/*:with_freetype": True,
        "freetype/*:shared": False,
        "icu/*:shared": False,
        "expat/*:shared": False,
    }

    def requirements(self):
        self.requires("icu/78.2")
        self.requires("freetype/2.13.2")
        self.requires("harfbuzz/11.4.1")
        self.requires("gflags/2.2.2")
        self.requires("fast_float/8.2.10")
        self.requires("vulkan-headers/1.4.357.0")
        self.requires("expat/2.6.3")
        self.requires("pugixml/1.14")
        self.requires("utfcpp/4.0.5")
        self.requires("boost/1.86.0")
        self.requires("zlib/1.3.1")
        if self.options.with_tests:
            self.requires("gtest/1.15.0")

    def configure(self):
        if self.settings.os not in ("Linux", "Macos"):
            raise ConanInvalidConfiguration(
                f"{self.ref} only supports Linux/macOS desktop builds (got {self.settings.os})"
            )
        if self.options.with_tests and self.options["gtest/*"].shared:
            raise ConanInvalidConfiguration("with_tests requires a static gtest")

    def layout(self):
        cmake_layout(self)
