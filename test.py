from engine import main
from engine.debugger import *
from engine.instructions import *
from engine.instructions.funcinstruction import *

Debugger.init()

showInst = FuncInstruction("show",'"Hello"')
showInst.exec()
