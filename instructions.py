from define import *
from register import *

class Filepos:
    def __init__(self, line, char):
        self.line = line
        self.char = char

class Instruction:       # general instructions
    def __init__(self, instruction_str, filepos):
        self.filepos = filepos
        self.str     = instruction_str
    
    def parse_params(self, params_str):
        """Parse only raw parameters (only str, int, bool or float)"""
        params = []
        cur = ""
        flag = False
        for c in params_str:
            if c == ',' and not flag:
                params.append(Variable.parse_to_type(cur))
                continue
            if c in '"':
                flag = not flag
                continue
            cur += c
        return params

    def exec(self):
        pass

class CondInstruction(Instruction):   # parsing conditionnal stuff
    def __init__(self, instruction_str, filepos):
        Instruction.__init__(self, instruction_str, filepos)
        
        self.left, self.right, self.operator = "", "", ""
        for c in self.str:
            if c in "!=<>":
                self.operator+=c
                continue
            # get both side of cond
            if len(self.operator) != 2: self.left  += c
            else:                       self.right += c
    
    def _parse_side(self, side_str, registry):
        t = Variable.get_type(side_str)
        if t == GSC_TYPES["STR"]:
            return registry.get_var(side_str.rstrip().lstrip())
        else:
            return Variable.parse_to_type(side_str)

    def exec(self, registry):
        l = self._parse_side(self.left,  registry)
        r = self._parse_side(self.right, registry)
        if self.operator == "==": return l == r
        if self.operator == "!=": return l != r
        if self.operator == "<=": return l <= r
        if self.operator == ">=": return l >= r
        return 0

class FuncInstruction:   # all functions in std
    def __init__(self, instruction_str, filepos):
        pass

class BranchInstruction: # if / for / while
    def __init__(self, instruction_str, filepos, block_codes):
        pass