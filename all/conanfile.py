from conans.tools import check_min_cppstd
from conans import ConanFile, tools
import os


class SharedClass(ConanFile):
    name = "game_01_shared_class"
    license = "BSL-1.0"
    author = "werto87"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "what does the lib do"
    topics = ("some tags")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "cmake"
    no_copy_source = True


    @property
    def _source_subfolder(self):
        return "source_subfolder"


    def source(self):
        if self.version != "latest":
            tools.get(**self.conan_data["sources"][self.version])
            extracted_dir = self.name + "-" + self.version
            os.rename(extracted_dir, self._source_subfolder)
        else:
            tools.get(url="https://github.com/werto87/game_01_shared_class/archive/refs/heads/main.zip")
            extracted_dir = self.name +"-main"
            os.rename(extracted_dir, self._source_subfolder)

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.settings.compiler.cppstd:
            check_min_cppstd(self, "11")
        self.options["boost"].header_only = True

    def requirements(self):
        self.requires("boost/1.76.0")
        self.requires("durak/0.0.4@werto87/stable")

    def package(self):
        self.copy(pattern="*", dst="include",
                  src=os.path.join(self._source_subfolder))                

    def package_id(self):
        self.info.header_only()
