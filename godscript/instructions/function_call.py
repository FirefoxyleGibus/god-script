from godscript.instructions.instruction import Instruction
from godscript.lib import Lib

class FunctionCall(Instruction):
	def __init__(self, pos : tuple, opt : tuple) -> None:
		funcname, params = opt
		super().__init__(pos, f"f {funcname} {' '.join([str(p) for p in params])}")
		self.func = Lib.get_func(funcname)

		self.params = params;

	def exec(self, context):
		return self.func(self.context, self.params)