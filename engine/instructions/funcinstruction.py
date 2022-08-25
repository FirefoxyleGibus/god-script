from engine.instructions.instruction import *

class FuncInstruction(Instruction):   # all functions in std
	def __init__(self, instruction_str, filepos, params):
		self.instr = instruction_str
		self.filepos = filepos
		self.params = Instruction.parse_params(params)

class BranchInstruction: # if / for / while
	def __init__(self, instruction_str, filepos, block_codes):
		pass