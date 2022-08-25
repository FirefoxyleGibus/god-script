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

class MissingVariableError(DebuggerException):
	def __init__(self, line, variable_name):
		self.line = line
		self.variable_name = variable_name

	def __str__(self):
		Debugger.log_error(f'Missing variable "{self.variable_name}" on line {self.line}')
		return f'{self.variable_name}\nMissing variable on line {self.line}'

class MissingFuncError(DebuggerException):
	def __init__(self, line, name):
		self.line = line
		self.name = name

	def __str__(self):
		Debugger.log_error(f'Function "{self.name}" on line {self.line} doesn\'t exist')
		return f'{self.name}\nFunction doesn\'t exist on line {self.line}'
