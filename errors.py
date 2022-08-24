from debugger import *

_debugger = Debugger()

class DebuggerException(Exception):
	pass

class InvalidSyntaxError(DebuggerException):
	def __init__(self, line, func, msg):
		self.msg = msg
		self.func = func
		self.line = line

	def __str__(self):
		_debugger.log_error(f'{self.func} on {self.line} : {self.msg}')
		return f'{self.func}\nInvalid Syntax on line : {self.line}\n{self.msg}'
