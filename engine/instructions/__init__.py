from engine.instructions.condinstruction import *
from engine.instructions.funcinstruction import *

from engine.register import *

class Filepos:
	def __init__(self, line, char):
		self.line = line
		self.char = char

class Instruction:       # general instructions
	def __init__(self, instruction_str, filepos=Filepos(0, 0)):
		self.filepos = filepos
		self.str     = instruction_str

	def parse_params(self, params_str):
		"""Parse only raw parameters (only str, int, bool or float)"""
		params = []
		cur = ""
		flag = False
		for c in params_str:
			if c == ',' and not flag:
				params.append(Variable.parse_to_type(cur))
				continue
			if c in '"':
				flag = not flag
				continue
			cur += c
		return params

	def exec(self):
		pass