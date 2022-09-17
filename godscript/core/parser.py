from ctypes.wintypes import WORD
import re
from godscript.core.types import ValueType, ReferenceType
from godscript.errors.core_errors import SyntaxRuleError
from godscript.lib import Lib

SPECIAL_CHARS = "(),;-+ \n\t'"
NUMBER_CHECK = "[0-9]+"
WORD_CHECK = "[A-Za-z_][0-9A-Za-z_]*"
STRING_CHECK = "\".*\""
VALUE_CHECK = f"\s*(({WORD_CHECK})|({NUMBER_CHECK})|({STRING_CHECK}))\s*"
PARAMS_CHECK = f"(\s*{VALUE_CHECK}\s*)(,\s*{VALUE_CHECK}\s*)*"
FUNCTION_CALL_CHECK = f"\s*{WORD_CHECK}\({PARAMS_CHECK}\)\s*"

class Parser:
    def check_rules(self, content):
        parenthesis_stack = 0
        str_flag = 0
        known_words = Lib.get_list().keys()
        comment = False

        word = ""
        for c_i, c in enumerate(content):
            # parenthesis checking
            if c == "(":
                parenthesis_stack+=1
            elif c == ")":
                parenthesis_stack-=1
                if parenthesis_stack < 0:
                    raise SyntaxRuleError(c_i, "Missing opening parenthesis before.")
            
            # comment check
            if c == "#":
                comment = True
            if comment:
                if c != "\n": continue
                else: comment = False

            # String check
            if c == '"':
                str_flag = not str_flag

            # word checking
            if not c in SPECIAL_CHARS:
                word += c
            else:
                if str_flag: continue # ignore

                # This is a number or a string
                if re.match(NUMBER_CHECK, word) or re.match(STRING_CHECK, word):
                    word = ""
                if len(word) > 0 and not word in known_words:
                    if c == "(":
                        raise SyntaxRuleError(c_i, "Function not known: " + repr(word))
                    else:
                        print(f"Warning: {word} not known.")
                word = ""

        if parenthesis_stack != 0:
            raise SyntaxRuleError(None, "Missing closing parenthesis.")
        
        if str_flag:
            raise SyntaxRuleError(None, "Missing closing string.")

    def split_lines(self, content):
        # line is (line_idx, content, opt_params)
        lines = []

        starting_pos = (0, 0)
        line_count = 0
        char_pos = 0
        accumulate = ""
        comment = True
        for i, c in enumerate(content):
            if c == "#":
                if len(accumulate.rstrip()) != 0:
                    raise SyntaxRuleError(starting_pos, "Missing ; at the end of the last instruction.")
                accumulate = ""
                starting_pos = (line_count+1, 0)
                comment = 1
            if comment and c != "\n":
                continue

            if c == ";":
                accumulate = accumulate.lstrip()
                if not re.match(FUNCTION_CALL_CHECK, accumulate):
                    raise SyntaxRuleError(starting_pos, f"Not correct function call : {accumulate}")
                lines.append((starting_pos, accumulate, self._parse_params(accumulate)))

                # Starting new instruction
                if len(content) > i+1:
                    if content[i+1] == "\n":
                        starting_pos = (line_count+1, 0)
                    else:
                        starting_pos = (line_count, char_pos+1)
                accumulate = ""

            if not c in ";":
                accumulate += c
            
            # pos
            if c == "\n":
                comment = False
                if len(accumulate) != 1:
                    raise SyntaxRuleError(starting_pos, "Missing ; at the end of the last instruction.")
                char_pos = 0
                line_count += 1
                accumulate = ""
            else:
                char_pos += 1

        if accumulate != "":
            raise SyntaxRuleError(starting_pos, f"Missing ; at the end of the instruction : {accumulate}")

        print(lines)
        return lines
    
    def _parse_params(self, line):
        funcname = ""
        params   = []

        for param in re.finditer(VALUE_CHECK, line):
            if not funcname:
                funcname = param.group(0)
                continue

            param_ = param.group(0).lstrip().rstrip();
            if re.match(WORD_CHECK, param_):
                params.append(ReferenceType(param_))
                continue
            params.append(ValueType(param_))
        
        return (funcname, params)