from define import *
from register import *
from debugger import *

_debugger = Debugger()

class tokenizer:
	code = ""
	lines = []
	instructions = []

	def __init__(self,file):
		_debugger.begin_section("TOKENISER INIT")
		_debugger.log("Opening ", file)
		with open(file,"rb") as f:
			strFlag = False
			comFlag = False
			for character in f.read().decode("UTF-8"):
				if (strFlag):
					if (character == "\r"):
						raise SyntaxError("str doesn't work on multiline, use "+ repr('\n') +" instead")
					elif (character == '"'):
						self.code += character
						strFlag = False
					else:
						self.code += character
				elif (comFlag):
					if (character == "#"):
						comFlag = False
					else:
						continue
				else:
					if (character == '"'):
						self.code += character
						strFlag = True
					elif (character == "#"):
						comFlag = True
					elif (character == "\r" or character == "\n" or character == "\t" or character == " "):
						continue
					else:
						self.code += character
#		with open(file,"r") as f:
#			for i in f.readlines():
#				self.code += i.replace("\n","").replace("\t","")
		_debugger.log("Read file")
		cur = ""
		for i in self.code:
			if (i != ";"):
				cur += i
			else:
				self.lines.append(cur)
				cur = ""
		_debugger.log("Splitted into instructions")
		for i in range(len(self.lines)):
			self.instructions += self.doOneCut(self.lines[i])
		_debugger.log("Cutted")
		_debugger.end_section()

	def doOneCut(self,inp):
		cur = ""
		out = []
		flag = False
		count = 0
		for j in inp:
			if (j == "("):
				count += 1
			elif (j == ")"):
				count -= 1
			if (j == "(" and not flag and count == 1):
				out.append(cur)
				cur = ""
				flag = True
			elif (j == ")" and flag and count == 0):
				out.append(self.doOneCut(cur))
				flag = False
				cur = ""
			else:
				cur += j
		else:
			if (cur != ""):
				out.append(cur)
		return out

	def showCode(self):
		_debugger.begin_section("TOKENISER OUT")
		_debugger.log(self.code)
		_debugger.log(self.lines)
		_debugger.log(self.instructions)
		_debugger.end_section()

	def sendData(self):
		return self.instructions

class parser:
	instructions = []

	def parse(self,instructions):
		self.instructions = instructions
		return self.parseOne(self.instructions)

	def parseOne(self,inp):
		out = []
		for i in range(len(inp)):
			if (type(inp[i]) == str):
				flag = False
				newStr = ""
				for j in inp[i]:
					if (j == '"'):
						flag = not flag
						newStr += j
					elif (j == " " and not flag):
						pass
					elif (j == "," and not flag):
						try:
							newStr = int(newStr)
						except:
							pass
						out.append(newStr)
						newStr = ""
					elif (flag):
						newStr += j
					else:
						newStr += j
				try:
					newStr = int(newStr)
				except:
					pass
				out.append(newStr)
			elif (type(inp[i]) == list):
				out.append(self.parseOne(inp[i]))
		return out

class interpreter:
	instructions = []

	def exec(self,instructions):
		_debugger.begin_section("INTERPRETER")
		self.register     = Register()

		# Replacing newLine with \n
		self.register.decl_var("newLine", '"\n"')
		_debugger.begin_section(f"REPLACE newLine")
		self.instructions = self.replaceVar(instructions,"newLine")
		_debugger.end_section()

		for i in range(len(self.instructions)):
			if (type(self.instructions[i]) == str):
				if (self.instructions[i] in funcDefiner.keys()):
					A = self.executeInst(self.instructions[i],self.instructions[i+1])

				elif (self.instructions[i] == "store"):
					if (len(self.instructions[i+1]) == 2):
						if (type(self.instructions[i+1][0]) == str):
							_debugger.log(f"Storing {self.instructions[i+1][1]} at {self.instructions[i+1][0]}")
							self.register.store_var(self.instructions[i+1][0], self.instructions[i+1][1])
							_debugger.begin_section(f"REPLACE {self.instructions[i+1][0]}")
							self.instructions = self.replaceVar(self.instructions,self.instructions[i+1][0])
							_debugger.end_section()
						else:
							_debugger.log_error("store: variable can't be numbers")
							raise SyntaxError("variable can't be numbers")

					elif (type(self.instructions[i+1][1] == str)):
						A = self.executeInst(self.instructions[i+1][1],self.instructions[i+1][2])
						if (type(self.instructions[i+1][0]) == str):
							_debugger.log(f"Storing {A} at {self.instructions[i+1][0]}")
							self.register.store_var(self.instructions[i+1][0], A)
							_debugger.begin_section(f"REPLACE {self.instructions[i+1][0]}")
							self.instructions = self.replaceVar(self.instructions,self.instructions[i+1][0])
							_debugger.end_section()
						else:
							_debugger.log_error("store: variable can't be numbers")
							raise SyntaxError("variable can't be numbers")

					else:
						_debugger.log_error(f"store: takes 2 paramaters, {len(self.instructions[i+1])} where given")
						raise SyntaxError("store takes 2 parameters")
				else:
					_debugger.log_error("nop, fck u for that shit : ", self.instructions[i])
					print("nop")
		_debugger.end_section()
		_debugger.close()

	def executeInst(self,inst,par):
		newPar = []
		flag = False
		for i in range(len(par)):
			if (flag):
				flag = False
				continue
			elif (type(par[i]) == str):
				if (par[i][0] != '"'):
					if (par[i] in funcDefiner.keys()):
						newPar.append(self.executeInst(par[i],par[i+1]))
						flag = True
					else:
						_debugger.log_error("Execute Instance: ", "function or variable '" + repr(par[i]) + "' doesn't exists")
						raise SyntaxError("function or variable '" + repr(par[i]) + "' doesn't exists")
				else:
					newPar.append(par[i])
			else:
				newPar.append(par[i])
		_debugger.log_func_call(inst, newPar)
		return funcDefiner[inst](newPar)


	def replaceVar(self, inp, var):
		"""Replace variable name by variable value"""
		_debugger.log(f"Replacing {var} in {repr(inp)} by {repr(self.register.get_var(var))}")
		B = []
		for i in inp:
			if (type(i) == list):
				[B.append(self.replaceVar(i,var))]
			else:
				if (i == var):
					B.append(self.register.get_var(var))
				else:
					B.append(i)
		return B
