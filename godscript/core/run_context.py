from godscript.core.parser import Parser
from godscript.core.tokeniser import Tokeniser
from godscript.lib import Lib

# context allow local storage and
# abstracts to client parser and everything
# allow to link other godscript file maybe ?
class RunContext:
	def __init__(self, filename):
		file_content = ""

		with open(filename, "r") as f:
			file_content = f.read()

		Lib.load()
		
		self.parser = Parser()
		self.parser.check_rules(file_content)
		lines = self.parser.split_lines(file_content)


		self.tokeniser = Tokeniser()
		tokens = self.tokeniser.tokenise_instructions(lines)
		print([str(tk) for tk in tokens])
