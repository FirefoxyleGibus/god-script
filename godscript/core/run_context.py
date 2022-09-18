from godscript.core.debugger import Debugger
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

		Debugger.init()
		Lib.load()
		
		Debugger.begin_section("Parser")
		self.parser = Parser()
		self.parser.check_rules(file_content)
		lines = self.parser.split_lines(file_content)
		Debugger.end_section()

		Debugger.begin_section("Tokeniser")
		self.tokeniser = Tokeniser()
		tokens = self.tokeniser.tokenise_instructions(lines)
		Debugger.end_section()
		print([str(tk) for tk in tokens])
