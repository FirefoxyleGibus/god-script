from engine.instructions.branchInstruction import BranchInstruction
from engine.instructions.condinstruction   import CondInstruction
from engine.instructions.instruction       import Filepos

class IfInstruction(BranchInstruction):
	def __init__(self, instruction_str, sub_instructions, filepos=Filepos(0,0)):
		super().__init__(instruction_str, sub_instructions, filepos)

		self.cond = CondInstruction(instruction_str, filepos)

	def __str__(self):
		return f'{self.instr} with {len(self.sub_instructions)} to run beginning at {self.filepos}'

	def __repr__(self):
		return f'{self.instr} : {self.sub_instructions}'

	def exec(self):
		if self.cond.exec():
			for instr in self.sub_instructions:
				instr.exec()
		
