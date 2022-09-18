import re
from godscript.instructions import *

class Tokeniser:
	def tokenise_instructions(self, instructions):
		tokenised_instr = []

		for instr_data in instructions:
			pos, instr, opt = instr_data
			for defined_instr_class in DEFINED_INSTRUCTIONS:
				if re.match(defined_instr_class.get_regex(), instr):
					tokenised_instr.append(defined_instr_class(pos, opt))
		
		return tokenised_instr