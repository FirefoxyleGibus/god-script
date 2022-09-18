import re
from godscript.core.debugger import Debugger
from godscript.instructions import *

class Tokeniser:
	def tokenise_instructions(self, instructions):
		Debugger.begin_section("Tokenising instructions")
		tokenised_instr = []

		for instr_data in instructions:
			pos, instr, opt = instr_data
			for defined_instr_class in DEFINED_INSTRUCTIONS:
				if re.match(defined_instr_class.get_regex(), instr):
					tokenised_instr.append(defined_instr_class(pos, opt))
		
		Debugger.log("\n".join([str(tk) for tk in tokenised_instr]))
		Debugger.end_section()
		return tokenised_instr