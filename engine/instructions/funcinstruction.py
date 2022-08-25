from engine.instructions import Instruction, Filepos

class FuncInstruction(Instruction):   # all functions in std
	def __init__(self, instruction_str, params, filepos=Filepos(0, 0)):
		self.instr = instruction_str
		self.filepos = filepos
		self.params = Instruction.parse_params(params)

class BranchInstruction: # if / for / while
	def __init__(self, instruction_str, sub_instructions, filepos=Filepos(0, 0)):
		pass