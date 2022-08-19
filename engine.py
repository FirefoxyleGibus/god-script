from define import *

class tokenizer:
	code = ""
	lines = []
	instructions = []

	def __init__(self,file):
		with open(file,"r") as f:
			for i in f.readlines():
				self.code += i.replace("\n","").replace("\t","")
		cur = ""
		for i in self.code:
			if (i != ";"):
				cur += i
			else:
				self.lines.append(cur)
				cur = ""
		for i in range(len(self.lines)):
			self.instructions += self.doOneCut(self.lines[i])

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
		print(self.code)
		print(self.lines)
		print(self.instructions)

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
		self.instructions = replaceVar(instructions,"newLine")

		for i in range(len(self.instructions)):
			if (type(self.instructions[i]) == str):
				if (self.instructions[i] in funcDefiner.keys()):
					A = self.executeInst(self.instructions[i],self.instructions[i+1])
				elif (self.instructions[i] == "store"):
					if (len(self.instructions[i+1]) == 2):
						if (type(self.instructions[i+1][0]) == str):
							variable[self.instructions[i+1][0]] = self.instructions[i+1][1]
							self.instructions = replaceVar(self.instructions,self.instructions[i+1][0])
						else:
							raise SyntaxError("variable can't be numbers")
					else:
						raise SyntaxError("store takes 2 parameters")
				else:
					print("nop")

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
						raise SyntaxError("fonctions or variable '" + par[i] + "' doesn't exists")
				else:
					newPar.append(par[i])
			else:
				newPar.append(par[i])
		return funcDefiner[inst](newPar)


def replaceVar(inp,var):
	B = []
	for i in inp:
		if (type(i) == list):
			[B.append(replaceVar(i,var))]
		else:
			if (i == var):
				B.append(variable[var])
			else:
				B.append(i)
	return B

variable = {"newLine":'"\n"'}
