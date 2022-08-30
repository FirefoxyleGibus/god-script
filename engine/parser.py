from engine.debugger import *
from engine.register import *

class Parser:
	instructions = []

	def parse(self,instructions):
		Debugger.begin_section("PARSING")
		self.instructions = instructions
		A = self.parseOne(self.instructions)
		Debugger.log("instr : [ " + ", ".join(repr(p) for p in self.instructions) + " ]")
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
						out.append(Variable.parse_to_type(newStr))
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