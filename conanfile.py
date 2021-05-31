import shutil
import os
from conans.tools import download, unzip, check_md5, check_sha1, check_sha256
from conans import ConanFile, CMake, tools


class SharedClass(ConanFile):
    name = "game_01_shared_class"
    version = "0.0.1"
    license = "BSL-1.0"
    author = "werto87"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "what does the lib do"
    topics = ("some tags")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    scm = {
        "type": "git",
        "subfolder": "game_01_shared_class",
        "url": "https://github.com/werto87/game_01_shared_class.git",
        "revision": "main"
    }

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        # We can control the options of our dependencies based on current options
        self.options["boost"].header_only = True

    def requirements(self):
        self.requires("catch2/2.13.1")
        self.requires("cereal/1.3.0")
        self.requires("boost/1.76.0")
        self.requires("durak/0.0.1")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_WASM"] = self.settings.os == "Emscripten"
        cmake.configure(source_folder="game_01_shared_class")
        cmake.build()

    def package(self):
        # This should lead to an Include path like #include "include_folder/IncludeFile.hxx"
        self.copy("*.h*", dst="include/game_01_shared_class",
                  src="game_01_shared_class/game_01_shared_class")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["game_01_shared_class"]
