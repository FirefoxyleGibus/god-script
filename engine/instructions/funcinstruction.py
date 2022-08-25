from engine.instructions.instruction import *
from engine.define import *
from engine.engine import *

class FuncInstruction(Instruction):   # all functions in std
	def __init__(self, instruction_str, params, filepos=Filepos(0, 0)):
		self.instr = instruction_str
		self.filepos = filepos
		self.params = self.parse_params(params)

	def __str__(self):
		return f'{self.instr} with {self.params} in {self.filepos}'

	def exec(self):
		if (self.instr not in funcDefiner.keys()):
			raise MissingFuncError(self.filepos.line,self.instr)
		else:
			return executeInst(self)


def executeInst(inst):
	global __register
	newPar = []
	for i in range(len(inst.params)):
		if (type(inst.params[i]) == FuncInstruction):
			if (inst.params[i] in funcDefiner.keys()):
				newPar.append(self.executeInst(inst.params[i]))
			else:
				raise MissingFuncError(inst.params[i].filepos.line,inst.params[i].instr)
		elif (type(inst.params[i]) == str):
			if not (inst.params[i][0] == '"'):
				newPar.append(__register.get_var(inst.params[i]).get_value())
			else:
				newPar.append(inst.params[i][i])
		else:
			newPar.append(inst.params[i][i])
	Debugger.log_func_call(inst, newPar)
	return funcDefiner[inst.instr](inst.params)


class BranchInstruction: # if / for / while
	def __init__(self, instruction_str, sub_instructions, filepos=Filepos(0, 0)):
		pass
