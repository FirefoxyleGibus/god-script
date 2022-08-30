from engine.engine import *

def setup(debug_mode):
	from engine.debugger import Debugger
	from engine.register import Register
	Debugger.init(debug_mode)
	Register.global_init()

# Entry point
def main(args):
	import time
	# Find filename else raise error
	filename = "" # default to test.gsc
	debug_mode = False
	for arg in args:
		if ".gsc" in arg: # if gsc file
			filename = arg
		if arg == "--debug": # if debug active
			debug_mode = True
	if not filename:
		raise SyntaxError("Please specify a filename")

	setup(debug_mode)

	t1 = time.perf_counter()
	T = tokenizer(filename)
	P = parser()
	I = interpreter()
	t2 = time.perf_counter()
	I.exec(T.sendData())
	t3 = time.perf_counter()

	print("\n\n=========")
	print("Data read in {0:.5f}s\nExecuted in {1:.5f}s\nTotal time spent {2:.5f}s".format(t2-t1,t3-t2,t3-t1))
	input("Press enter to close the process ... ")
