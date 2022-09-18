from email.mime import base
from genericpath import getmtime
import re, os
from godscript.core.debugger import Debugger
from godscript.instructions import *

class Tokeniser:
	def tokenise_file(self, filename, filepath, instructions):
		basename = filename.split("/")[-1]
		basename = basename.split("\\")[-1]
		basename = basename.split(".")[0]
		out_filename = basename+".token"
		out_filepath = f"./__gsccache__/{out_filename}";

		if not Debugger.debug_mode:
			if os.path.isfile(out_filepath) \
			and getmtime(out_filepath) > getmtime(filepath):
				Debugger.log("Not updating tokenisation")
				return

		with open(out_filepath, "w") as f:
			f.writelines([str(t) for t in instructions])

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