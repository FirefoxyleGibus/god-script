from engine.engine import *

# Entry point
def main(args):
    from engine.debugger import Debugger
    import time

    # Find filename else raise error
    filename = "" # default to test.gsc
    for arg in args:
        if arg.split(".")[1] == "gsc":
            filename = arg
    if not filename:
        raise SyntaxError("Please specify a filename")

    Debugger.init()

    t1 = time.perf_counter()
    T = tokenizer(filename)
    P = parser()
    I = interpreter()
    t2 = time.perf_counter()
    I.exec(P.parse(T.sendData()))
    t3 = time.perf_counter()

    print("\n\n=========")
    print("Data read in {0:.5f}s\nExecuted in {1:.5f}s\nTotal time spent {2:.5f}s".format(t2-t1,t3-t2,t3-t1))
    input("Press enter to close the process ... ")
