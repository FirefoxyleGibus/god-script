import os

class Debugger:
	def init(debug_mode=False, indent="\t"):
		"""Initialize the debugger, must be called before any of its methods.

		Args:
			indent (str, optional): indentation character for sections. Defaults to "\t".
		"""
		Debugger.debug_mode = debug_mode
		if not (os.path.isdir(r"./__gsccache__")):
			os.mkdir(r"./__gsccache__")

		Debugger.file = open(r"./__gsccache__/stacktrace.txt", "w")
		Debugger.current_sections_stack = []
		Debugger.indent_str = indent
	
	def write_tokenised_file(filename : str, tokens : list):
		with open(f"./__gsccache__/{filename}_tokenised.py", "w") as f:
			f.write([str(tk) for tk in tokens])
	
	def _write_output(output):
		"""Write to file and to stdout if out is true"""
		s = Debugger._indent() + output + "\n"
		if not Debugger.file.closed:
			Debugger.file.write(s)

	def _indent():
		"""Return the Indentation based on how many sections are opened
		Returns str
		"""
		return len(Debugger.current_sections_stack) * Debugger.indent_str

	def begin_section(section_name):
		"""Begin a new section
		Args:
			section_name (str): Section name
		"""
		s = f"[ BEGIN SECTION {section_name} ]"
		Debugger._write_output(s)
		Debugger.current_sections_stack.append(section_name)

	def end_section():
		"""End the last opened section
		Returns None
		"""
		if len(Debugger.current_sections_stack) == 0: return # No section to close
		section_name = Debugger.current_sections_stack.pop()

		s = f"[ ENDING SECTION {section_name} ]"
		Debugger._write_output(s)

	def log(*msg, sep=" "):
		"""Log the message to the debug file
		Args:
			sep (str, optional): separation between msg elements. Defaults to " ".
		"""
		s = str(sep).join(msg)
		Debugger._write_output(s)

	def log_error(*msg, sep=" "):
		"""Log error to the debug file
		Args:
			sep (str, optional): separation between msg elements. Defaults to " ".
		"""
		s = "[ERROR] " + str(sep).join(msg)
		Debugger._write_output(s)

	def log_instruction(instruction, *msg, sep=" "):
		s  = instruction.instr + " "
		s += f"[{str(instruction.filepos)}]: " + sep.join([str(p) for p in msg])
		Debugger._write_output(s)

	def log_instruction_error(instruction, *msg, sep=" "):
		s = "[ERROR] " + instruction.instr + " "
		s += f"[{str(instruction.filepos)}]: " + sep.join([str(p) for p in msg])
		Debugger._write_output(s)

	def log_func_call(funcname, parameters_list):
		"""Log the call to the <funcname> with their parameters
		Args:
			funcname (str): function name that has been called
			parameters_list (list): list of the parameters that was given for this function call
		"""
		Debugger._write_output(f"Called {funcname} with {', '.join([repr(p) for p in parameters_list])}")

	def close():
		"""Close the Debugger (must be called at the end of the program)"""
		Debugger.file.close()