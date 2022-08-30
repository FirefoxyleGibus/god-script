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
		branch_lines = []
		branch_flag  = False
		for line_i, i in enumerate(self.code):
			# Branch
			if (i == "{"):
				branch_flag = True
				branch_lines.append(cur)
				cur = ""
			elif (i == "}"):
				if not branch_flag:
					raise InvalidSyntaxError(line_i, "fetch", "Missing opening bracket.")
				
				self.lines.append(branch_lines)
				branch_lines = []
				branch_flag  = False
				cur          = ""

			# end of line (EOL)
			elif (i != ";"):
				cur += i
			else:
				if branch_flag:
					branch_lines.append(cur)
				else:
					self.lines.append(cur)
				cur = ""
		else:
			if (cur != ""):
				raise InvalidSyntaxError(0,"fetch","Missing ; at the end of file")
		
		Debugger.log("Splitted into instructions")
		
		for i, line in enumerate(self.lines):
			if (type(line) == list):
				self.instructions += self._doBranchCut(line, i+1, 0)
			else:
				self.instructions += self._doOneCut(line, i+1, 0)
		
		Debugger.log("Cutted")
		Debugger.log("instr : [ " + ", ".join(repr(p) for p in self.instructions) + " ]")
		Debugger.end_section()

	def _doBranchCut(self, instructions, line, deep):
		branch_exec     = instructions[0].split("(")
		branch_subinstr = instructions[1:]

		branch_type  = branch_exec[0]
		branch_cond  = branch_exec[1][:-1]

		# parse sub instructions
		branch_instr = []
		for i, instr in enumerate(branch_subinstr):
			branch_instr += self._doOneCut(instr, line+i, deep)
		
		if branch_type == "if":
			return [IfInstruction(branch_cond, branch_instr, Filepos(line, deep))]
		return []

	def _doOneCut(self, inp, line, deep):
		cur = ""
		out = []
		par = []
		instr = ""
		flag = False

		count = 0
		for j in inp:
			# Parsing params
			if (j == "("):
				count += 1
			elif (j == ")"):
				count -= 1
			
			if (j == "(" and not flag and count == 1):
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