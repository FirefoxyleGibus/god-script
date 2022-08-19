def func1(par):
	if (type(par) == list):
		out = ""
		for i in par:
			if (type(i) != str):
				out += str(i)
			else:
				if (i[0] != '"'):
					raise SyntaxError("show takes value or variable")
				out += i.replace('"',"")
		print(out,end="")
		return None
	else:
		raise SyntaxError("Unexpected error")

def func2(par):
	if (type(par) == list and len(par) < 3):
		for i in par:
			if not (type(i) == int or type(i) == float):
				raise SyntaxError("add takes float parameters")
		else:
			if (len(par) == 0):
				return 0
			elif (len(par) == 1):
				return par[0]
			elif (len(par) == 2):
				return par[0] + par[1]
	else:
		raise SyntaxError("add takes less than 3 arguments")

def func3(par):
	if (type(par) == list):
		out = ""
		for i in par:
			if (type(i) != str):
				out += str(i)
			else:
				if (i[0] != '"'):
					raise SyntaxError("show takes value or variable")
				out += i.replace('"',"")
		return '"' + input(out) + '"'
	else:
		raise SyntaxError("Unexpected error")

def func4(par):
	if (type(par) == list and len(par) == 1):
		return '"' + str(par[0]) + '"'
	else:
		raise SyntaxError("toString takes only 1 argument")

def func5(par):
	if (type(par) == list and len(par) == 1):
		try:
			return int(par[0].replace('"',""))
		except:
			raise SyntaxError("Invalid input")
	else:
		raise SyntaxError("toString takes only 1 argument")

funcDefiner = {
	"show":func1,
	"add":func2,
	"input":func3,
	"toString":func4,
	"toInt":func5
}
