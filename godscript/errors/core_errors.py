from godscript.errors.error import Error
from godscript.core.debugger import Debugger

class SyntaxRuleError(Error):
	def __init__(self, line, reason):
		self.line = line
		self.reason = reason
		Debugger.log_error(f"{self.line}: {self.reason}")

	def __str__(self):
		return f"SyntaxRuleError[{self.line}]: {self.reason}"