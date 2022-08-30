from engine.instructions.instruction import *

class VariableInstruction(Instruction):
	def __init__(self, instruction_str, filepos=Filepos(0, 0)):
		lvalue, rvalue = instruction_str.split("=")