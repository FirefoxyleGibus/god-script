class Instruction():
	def __init__(self, pos : tuple, string : str) -> None:
		self.pos = pos
		# str is used to allow tokenisation if we want to
		# like allowing one word to describe an instruction
		# and parsing it to a file with our tokenisation format
		# to read it and not have to build it each time we run it
		self.str = string

	def buildInstruction(self):
		instr = self.str.split(" ")
		if (instr[0] == "f"):
			finalInstr = (instr[1],[instr[i] for i in range(2,len(instr))])
			self.obj = FunctionCall(self.pos,finalInstr)

	def exec(self,context):
		self.obj.exec(context)

	def __str__(self) -> str:
		return self.str

	def get_regex():
		return ""
