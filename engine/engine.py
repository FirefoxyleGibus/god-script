from engine.define import *
from engine.register import *
from engine.debugger import *
from engine.errors import *
from engine.instructions import *

class Interpreter:
	instructions = []

	def exec(self,instructions):
		Debugger.begin_section("INTERPRETER")
		self.register     = Register.global_instance() # create global instance
		self.instructions = instructions

		for i in range(len(self.instructions)):
			self.instructions[i].exec()
		Debugger.end_section()
		Debugger.close()


	def replaceVar(self, inp, var):
		"""Replace variable name by variable value"""
		Debugger.log(f"Replacing {var} in {repr(inp)} by {repr(self.register.get_var(var))}")
		B = []
		for i in inp:
			if (type(i) == list):
				[B.append(self.replaceVar(i,var))]
			else:
				if (i == var):
					B.append(self.register.get_var(var))
				else:
					B.append(i)
		return B
