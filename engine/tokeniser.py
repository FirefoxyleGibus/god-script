from engine.debugger import *
from engine.register import *
from engine.errors   import *
from engine.instructions import *

class Tokeniser:
	code = ""
	lines = []
	instructions = []

	def __init__(self, file):
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
		else:
			if (cur != ""):
				raise InvalidSyntaxError(0,"fetch","Missing ; at the end of file")
		
		Debugger.log("Splitted into instructions")
		
		for i in range(len(self.lines)):
			self.instructions += self._doOneCut(self.lines[i], i+1, 0)
		
		Debugger.log("Cutted")
		Debugger.log("instr : [ " + ", ".join(repr(p) for p in self.instructions) + " ]")
		Debugger.end_section()

	def _doOneCut(self, inp, line, deep):
		cur = ""
		out = []
		par = []
		instr = ""
		flag = False

		branch_type  = ""
		branch_flag  = False
		branch_instr = []

		count = 0
		for j in inp:
			# Parsing branches
			if (j == "{"):
				if branch_flag:
					branch_instr += self._doOneCut(cur, line, deep+1)
				branch_type = instr
				instr = ""
				branch_flag = True
				continue
			elif (j == "}"):
				if branch_type == "if":
					cond = par[0]
					del par[0]

					# parse sub instructions
					binstr = []
					for b in branch_instr:
						if (b != ""):
							binstr.append(FuncInstruction(b,par,Filepos(line,deep)))
					
					out.append(IfInstruction(cond, binstr, Filepos(line, deep)))
					return out
					branch_instr = []
				branch_flag = False
				continue
			
			# Parsing params
			if (j == "("):
				count += 1
			elif (j == ")"):
				count -= 1
			
			if (j == "(" and not flag and count == 1):
				if branch_flag:
					branch_instr.append(cur)
				else:
					instr = cur
				cur = ""
				flag = True
			elif (j == "," and flag and count == 1):
				par += (self._doOneCut(cur, line, deep+1))
				cur = ""
			elif (j == ")" and flag and count == 0):
				par += (self._doOneCut(cur, line, deep+1))
				flag = False
				cur = ""
			else:
				cur += j
		else:
			if (cur != ""):
				return [Variable.parse_to_type(cur)]
		
		if len(out) != 0:
			return out

		# Functions or params
		if (instr != ""):
			out.append(FuncInstruction(instr, par, Filepos(line,deep)))
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