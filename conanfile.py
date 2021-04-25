import shutil
import os
from conans.tools import download, unzip, check_md5, check_sha1, check_sha256
from conans import ConanFile, CMake, tools


class MyNewLib(ConanFile):
    name = "my_new_lib"
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
        "url": "URL to Git Repo",
        "revision": "main"
    }

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def requirements(self):
        # Add some requirements
        #self.requires("boost/1.75.0")
        #self.requires("magic_enum/0.6.6")
        #self.requires("catch2/2.13.1")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="my_new_lib")
        cmake.build()

    def package(self):
        # This should lead to an Include path like #include "include_folder/IncludeFile.hxx"
        self.copy("*.h*", dst="include/include_folder",
                  src="include_folder/include_folder")
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Here You Should put the Name of the lib. Use the same name like in CMakeLists.txt of your lib"]
