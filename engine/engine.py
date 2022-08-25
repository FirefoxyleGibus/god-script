from engine.define import *
from engine.register import *
from engine.debugger import *
from engine.errors import *
from engine.instructions import *

__register = Register()

class tokenizer:
	code = ""
	lines = []
	instructions = []

	def __init__(self,file):
		Debugger.begin_section("TOKENISER INIT")
		Debugger.log("Opening ", file)
		with open(file,"rb") as f:
			strFlag = False
			comFlag = False
			oneComFlag = False
			privFlag = False
			for character in f.read().decode("UTF-8"):
				if (strFlag):
					if (character == "\r"):
						raise InvalidSyntaxError(0,"fetch","str doesn't work on multiline, use "+ repr('\n') +" instead")
					elif (character == '"'):
						self.code += character
						strFlag = False
					else:
						self.code += character
				elif (comFlag):
					if (privFlag and character == "#"):
						comFlag = False
						oneComFlag = False
						privFlag = False
					elif (character == "#"):
						privFlag = True
					else:
						continue
				elif (oneComFlag):
					if (character == "\r"):
						oneComFlag = False
					elif (character == "#"):
						comFlag = True
					else:
						continue
				else:
					if (character == '"'):
						self.code += character
						strFlag = True
					elif (character == "#"):
						oneComFlag = True
					elif (character == "\r" or character == "\n" or character == "\t" or character == " "):
						continue
					else:
						self.code += character
			self.code = bytes(self.code, "utf-8").decode("unicode_escape")
		Debugger.log("Read file")
		cur = ""
		for i in self.code:
			if (i != ";"):
				cur += i
			else:
				self.lines.append(cur)
				cur = ""
		Debugger.log("Splitted into instructions")
		for i in range(len(self.lines)):
			self.instructions += self.doOneCut(self.lines[i],i+1)
		Debugger.log("Cutted")
		Debugger.log("instr :", str(self.instructions))
		Debugger.end_section()

	def doOneCut(self,inp,line):
		cur = ""
		out = []
		par = []
		inst = ""
		flag = False
		count = 0
		for j in inp:
			if (j == "("):
				count += 1
			elif (j == ")"):
				count -= 1
			if (j == "(" and not flag and count == 1):
				inst = cur
				cur = ""
				flag = True
			elif (j == ")" and flag and count == 0):
				par += (self.doOneCut(cur,line))
				flag = False
				cur = ""
			else:
				cur += j
		else:
			if (cur != ""):
				return cur
		if (inst != ""):
			out.append(FuncInstruction(inst,par,Filepos(1,line)))
			return out
		else:
			return par

	def showCode(self):
		Debugger.begin_section("TOKENISER OUT")
		Debugger.log(self.code)
		Debugger.log(self.lines)
		Debugger.log(self.instructions)
		Debugger.end_section()

	def sendData(self):
		return self.instructions

class parser:
	instructions = []

	def parse(self,instructions):
		Debugger.begin_section("PARSING")
		self.instructions = instructions
		A = self.parseOne(self.instructions)
		Debugger.log("instr :",str(A))
		Debugger.end_section()
		return A

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
		Debugger.begin_section("INTERPRETER")
		self.register     = Register()
		self.instructions = instructions

		for i in range(len(self.instructions)):
			self.instructions[i].exec()
		Debugger.end_section()
		Debugger.close()


	def replaceVar(self, inp, var):
		"""Replace variable name by variable value"""
		Debugger.log(f"Replacing {var} in {repr(inp)} by {repr(self.register.get_var(var))}")
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
