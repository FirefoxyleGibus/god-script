from engine.instructions.instruction import *

class BranchInstruction(Instruction): # if / for / while
	def __init__(self, instruction_str, sub_instructions, filepos=Filepos(0, 0)):
		self.instr = instruction_str
		self.sub_instructions = sub_instructions
		self.filepos = filepos

	def __str__(self):
		return f'{self.instr} with {len(self.sub_instructions)} beggining {self.filepos}'

	def __repr__(self):
		return f'{self.instr} : [{["- " + repr(i) + ", " for i in self.sub_instructions]}]'

	def exec(self):
		for instr in self.sub_instructions:
			instr.exec()