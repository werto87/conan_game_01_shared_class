import shutil
import os
from conans.tools import download, unzip, check_md5, check_sha1, check_sha256
from conans import ConanFile, CMake, tools


class SharedClass(ConanFile):
    name = "shared_class"
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
        "subfolder": "folder with Includes",
        "url": "https://github.com/werto87/game_01_shared_class.git",
        "revision": "main"
    }

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def requirements(self):
        self.requires("confu_boost/0.0.1@confu_boost/0.0.1")
        

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="shared_class")
        cmake.build()

    def package(self):
        # This should lead to an Include path like #include "include_folder/IncludeFile.hxx"
        self.copy("*.h*", dst="include/shared_class",
                  src="shared_class/shared_class")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["shared_class"]
