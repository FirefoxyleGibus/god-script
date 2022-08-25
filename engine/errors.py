from engine.debugger import *

class DebuggerException(Exception):
	pass

class InvalidSyntaxError(DebuggerException):
	def __init__(self, line, func, msg):
		self.msg = msg
		self.func = func
		self.line = line

	def __str__(self):
		Debugger.log_error(f'{self.func} on {self.line} : {self.msg}')
		return f'{self.func}\nInvalid Syntax on line : {self.line}\n{self.msg}'

class ZeroDivision(DebuggerException):
	def __init__(self, line, msg):
		self.msg = msg
		self.line = line

	def __str__(self):
		Debugger.log_error(f'div on {self.line} : {self.msg}')
		return f'div\nInvalid Syntax on line : {self.line}\n{self.msg}'
