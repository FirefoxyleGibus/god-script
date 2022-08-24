def func1(par):
	if (type(par) == list):
		out = ""
		for i in par:
			if (type(i) != str):
				out += str(i)
			else:
				if (i[0] != '"'):
					raise SyntaxError("show takes value or variable")
				out += i[1:-1]
		print(out,end="")
		return None
	else:
		raise SyntaxError("Unexpected error")

def func2(par):
	if (type(par) == list and len(par) == 2):
		for i in par:
			if not (type(i) == int or type(i) == float):
				raise SyntaxError("add takes float parameters")
		else:
			if (len(par) == 2):
				return par[0] + par[1]
	else:
		raise SyntaxError("add takes 2 arguments")

def func3(par):
	if (type(par) == list):
		out = ""
		for i in par:
			if (type(i) != str):
				out += str(i)
			else:
				if (i[0] != '"'):
					raise SyntaxError("input takes value or variable")
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

def func6(par):
	if (type(par) == list and len(par) in range(1, 3)):
		for i in par:
			if not (type(i) == int or type(i) == float):
				raise SyntaxError("sub takes float parameters")
		else:
			if (len(par) == 1):
				return -par[0]
			elif (len(par) == 2):
				return par[0] - par[1]
	else:
		raise SyntaxError("sub takes one or two arguments")

def func7(par):
	if (type(par) == list and len(par) == 2):
		for i in par:
			if not (type(i) == int or type(i) == float):
				raise SyntaxError("mul takes float parameters")
		else:
			return par[0] * par[1]
	else:
		raise SyntaxError("mul takes 2 arguments")

def func8(par):
	if (type(par) == list and len(par) in range(1, 3)):
		for i in par:
			if not (type(i) == int or type(i) == float):
				raise SyntaxError("div takes float parameters")
		else:
			if (len(par) == 1):
				if par[0] == 0:
					raise ZeroDivisionError("Cannot divide by zero")
				return int(1/par[0])
			elif (len(par) == 2):
				if par[1] == 0:
					raise ZeroDivisionError("Cannot divide by zero")
				return int(par[0] / par[1])
	else:
		raise SyntaxError("div takes one or two arguments")

funcDefiner = {
	"show":    func1,
	"add":     func2,
	"input":   func3,
	"toString":func4,
	"toInt":   func5,
	"sub":     func6,
	"mul":     func7,
	"div":     func8
}
