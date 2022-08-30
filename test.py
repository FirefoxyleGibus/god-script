from engine import *
from engine.debugger import *
from engine.instructions import *
from engine.instructions.funcinstruction import *

Debugger.init()

if_instr = IfInstruction("1 == 0", [
    FuncInstruction("show", ['"test"', '"\n"'])
])

if_instr.exec()