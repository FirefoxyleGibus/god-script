from textwrap import indent


class Debugger:
    def __init__(self, indent="\t"):
        self.filename = open("__gsccache__/stacktrace.txt", "w")
        self.current_sections_stack = []
        self.indent_str = indent
    
    def indent(self):
        return len(self.current_sections_stack) * self.indent_str

    def begin_section(self, section_name):
        """Begin a new debug section"""
        self.filename.write(self.indent() + f"[ BEGIN SECTION {section_name} ]\n")
        self.current_sections_stack.append(section_name)
    
    def end_section(self):
        """End the last opened section"""
        if len(self.current_sections_stack) == 0: return # No section to close
        section_name = self.current_sections_stack.pop()
        self.filename.write(self.indent() + f"[ ENDING SECTION {section_name} ]\n")

    def log(self, *msg, sep=" "):
        s = str(sep).join(msg)
        self.filename.write(self.indent() + s + "\n")
    
    def log_error(self, *msg, sep=" "):
        s = str(sep).join(msg)
        self.filename.write(self.indent() + "[ERROR] " + s + "\n")
    
    def log_func_call(self, funcname, parameters_list):
        self.filename.write(self.indent() + f"Called {funcname} with {', '.join([repr(p) for p in parameters_list])}\n")

    def close(self):
        self.filename.close()