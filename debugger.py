
class Debugger:
    def init(indent="\t"):
        """Initialize the debugger, must be called before any of its methods.

        Args:
            indent (str, optional): indentation character for sections. Defaults to "\t".
        """
        Debugger.file = open("__gsccache__/stacktrace.txt", "w")
        Debugger.current_sections_stack = []
        Debugger.indent_str = indent
    
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
        Debugger.file.write(Debugger._indent() + f"[ BEGIN SECTION {section_name} ]\n")
        Debugger.current_sections_stack.append(section_name)
    
    def end_section():
        """End the last opened section

        Returns None
        """
        if len(Debugger.current_sections_stack) == 0: return # No section to close
        section_name = Debugger.current_sections_stack.pop()
        Debugger.file.write(Debugger._indent() + f"[ ENDING SECTION {section_name} ]\n")

    def log(*msg, sep=" "):
        """Log the message to the debug file

        Args:
            sep (str, optional): separation between msg elements. Defaults to " ".
        """
        s = str(sep).join(msg)
        Debugger.file.write(Debugger._indent() + s + "\n")
    
    def log_error(*msg, sep=" "):
        """Log error to the debug file

        Args:
            sep (str, optional): separation between msg elements. Defaults to " ".
        """
        s = str(sep).join(msg)
        Debugger.file.write(Debugger._indent() + "[ERROR] " + s + "\n")
    
    def log_func_call(funcname, parameters_list):
        """Log the call to the <funcname> with their parameters

        Args:
            funcname (str): function name that has been called
            parameters_list (list): list of the parameters that was given for this function call
        """
        Debugger.file.write(Debugger._indent() + f"Called {funcname} with {', '.join([repr(p) for p in parameters_list])}\n")

    def close():
        """Close the Debugger (must be called at the end of the program)"""
        Debugger.file.close()