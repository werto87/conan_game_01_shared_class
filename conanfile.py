from conans.tools import check_min_cppstd
from conans import ConanFile


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
        if self.settings.compiler.cppstd:
            check_min_cppstd(self, "11")
        self.options["boost"].header_only = True

    def requirements(self):
        self.requires("boost/1.76.0")
        self.requires("durak/0.0.4@werto87/stable")

    def package(self):
        self.copy("*.h*", dst="include/game_01_shared_class",
                  src="game_01_shared_class/game_01_shared_class")

    def package_id(self):
        self.info.header_only()
