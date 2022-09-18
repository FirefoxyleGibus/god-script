class Instruction():
	def __init__(self, pos : tuple, string : str) -> None:
		self.pos = pos
		# str is used to allow tokenisation if we want to
		# like allowing one word to describe an instruction
		# and parsing it to a file with our tokenisation format
		# to read it and not have to build it each time we run it
		self.str = string

	def exec(context):
		pass

	def __str__(self) -> str:
		return self.str

	def get_regex():
		return ""