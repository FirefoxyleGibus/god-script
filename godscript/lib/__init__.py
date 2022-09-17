from importlib import import_module
import os

stdpath = ("/".join(__path__)).removesuffix("__init__.py")

class Lib:
    lib_functions = {}

    def load():
        Lib.lib_functions = {}
        for f in os.listdir(stdpath):
            if f == "__init__.py": continue
            funcname = f.removesuffix(".py")
            Lib.lib_functions[funcname] = import_module("."+funcname, "godscript.lib")
    
    def get_list():
        return Lib.lib_functions

    def get_func(funcname):
        if funcname in Lib.lib_functions:
            return 