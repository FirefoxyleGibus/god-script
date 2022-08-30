from engine.instructions.instruction import *
from engine.define import *
from engine.engine import *

class FuncInstruction(Instruction):   # all functions in std
	def __init__(self, instruction_str, params, filepos=Filepos(0, 0)):
		self.instr = instruction_str
		self.filepos = filepos
		self.params = []
		for i in params:
			if (type(i) != FuncInstruction):
				self.params.append(Variable.parse_to_type(i))
			else:
				self.params.append(i)
		self.strParams = "[" + ",".join([repr(p) for p in self.params]) + "]"

	def __str__(self):
		return f'{self.instr} with {self.strParams} in {self.filepos}'

	def __repr__(self):
		return f'{self.instr} : {self.strParams}'

	def exec(self):
		Debugger.log_instruction(self,"Trying execution with parameters", self.strParams)
		if (self.instr not in funcDefiner.keys() and self.instr != "store"):
			raise MissingFuncError(self.filepos.line, self.instr)
		else:
			return executeInst(self)


def executeInst(inst):
	newPar = []
	if (inst.instr == "store"):
		if (len(inst.params) == 2):
			if (type(inst.params[0]) == str):
				if (type(inst.params[1]) == FuncInstruction):
					inst.params[1] = inst.params[1].exec()
				Register.global_instance().store_var(inst.params[0],inst.params[1])
				return None
			else:
				raise InvalidSyntaxError(inst.filepos.line,"store","variable can't be a number")
		else:
			raise InvalidSyntaxError(inst.filepos.line,"store","store takes a variable name and a value")
	else:
		for i in range(len(inst.params)):
			if (type(inst.params[i]) == FuncInstruction):
				newPar.append(inst.params[i].exec())
			elif (type(inst.params[i]) == str):
				if not (inst.params[i][0] == '"'):
					newPar.append(Register.global_instance().get_var(inst.params[i]))
				else:
					newPar.append(inst.params[i])
			else:
				newPar.append(inst.params[i])
		return funcDefiner[inst.instr](newPar)