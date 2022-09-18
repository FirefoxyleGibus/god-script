from importlib import import_module
import os

from godscript.core.debugger import Debugger

stdpath = ("/".join(__path__))

class Lib:
	lib_functions = {}

	def load():
		Debugger.begin_section("Lib loading")
		Lib.lib_functions = {}
		for f in os.listdir(stdpath):
			if f == "__init__.py" or os.path.isdir(f): continue
			funcname = f.removesuffix(".py")
			Debugger.log(f"Found {f}")
			Lib.lib_functions[funcname] = import_module("."+funcname, "godscript.lib")
		Debugger.end_section()
	
	def get_list():
		return Lib.lib_functions

	def get_func(funcname):
		if funcname in Lib.lib_functions.keys():
			return Lib.lib_functions[funcname]
		return (lambda x : None)