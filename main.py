# God script use .gsc

if __name__ == "__main__":
	import sys
	from godscript.core.run_context import RunContext
	filename = sys.argv[1]
	run = RunContext(filename)
