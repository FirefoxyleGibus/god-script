from instructions import CondInstruction, Filepos
from register import Register

if __name__ == "__main__":
    r = Register()
    c = CondInstruction("0 == 1 || 1 == 1", Filepos(0, 0))
    print(c.exec(r))