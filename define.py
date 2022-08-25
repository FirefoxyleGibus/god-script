from engine.errors import *

def func1(par):
	if (type(par) == list):
		out = ""
		for i in par:
			if (type(i) != str):
				out += str(i)
			else:
				if (i[0] != '"'):
					raise InvalidSyntaxError(0,"show","show takes value or variable")
				out += i[1:-1]
		print(out,end="")
		return None
	else:
		raise InvalidSyntaxError(0,"show","Unexpected error")

def func2(par):
	if (type(par) == list and len(par) == 2):
		for i in par:
			if not (type(i) == int or type(i) == float):
				raise InvalidSyntaxError(0,"add","add takes float parameters")
		else:
			if (len(par) == 2):
				return par[0] + par[1]
	else:
		raise InvalidSyntaxError(0,"add","add takes 2 arguments")

def func3(par):
	if (type(par) == list):
		out = ""
		for i in par:
			if (type(i) != str):
				out += str(i)
			else:
				if (i[0] != '"'):
					raise InvalidSyntaxError(0,"input","input takes value or variable")
				out += i.replace('"',"")
		return '"' + input(out) + '"'
	else:
		raise InvalidSyntaxError(0,"input","Unexpected error")

def func4(par):
	if (type(par) == list and len(par) == 1):
		return '"' + str(par[0]) + '"'
	else:
		raise InvalidSyntaxError(0,"toString","toString takes only 1 argument")

def func5(par):
	if (type(par) == list and len(par) == 1):
		try:
			return int(par[0].replace('"',""))
		except:
			raise InvalidSyntaxError(0,"toInt","the value is not an int")
	else:
		raise InvalidSyntaxError(0,"toInt","toInt takes only 1 argument")

def func6(par):
	if (type(par) == list and len(par) in range(1, 3)):
		for i in par:
			if not (type(i) == int or type(i) == float):
				raise InvalidSyntaxError(0,"sub","sub takes float parameters")
		else:
			if (len(par) == 1):
				return -par[0]
			elif (len(par) == 2):
				return par[0] - par[1]
	else:
		raise InvalidSyntaxError(0,"sub","sub takes one or two arguments")

def func7(par):
	if (type(par) == list and len(par) == 2):
		for i in par:
			if not (type(i) == int or type(i) == float):
				raise InvalidSyntaxError(0,"mul","mul takes float parameters")
		else:
			return par[0] * par[1]
	else:
		raise InvalidSyntaxError(0,"mul","mul takes 2 arguments")

def func8(par):
	if (type(par) == list and len(par) in range(1, 3)):
		for i in par:
			if not (type(i) == int or type(i) == float):
				raise InvalidSyntaxError(0,"div","div takes float parameters")
		else:
			if (len(par) == 1):
				if par[0] == 0:
					raise ZeroDivision(0,"Cannot divide by zero")
				return int(1/par[0])
			elif (len(par) == 2):
				if par[1] == 0:
					raise ZeroDivision(0,"Cannot divide by zero")
				return int(par[0] / par[1])
	else:
		raise InvalidSyntaxError(0,"div","div takes one or two arguments")

def func9(par):
	if (type(par) == list and len(par) == 1):
		try:
			return '"'+chr(par[0])+'"'
		except:
			raise InvalidSyntaxError(0,"toChar","value is not a character's code")
	else:
		raise InvalidSyntaxError(0,"toChar","toChar takes only 1 argument")

def func10(par):
	if (type(par) == list and len(par) == 1):
		try:
			return ord(par[0].replace('"',""))
		except:
			raise InvalidSyntaxError(0,"toUni","value is not a character")
	else:
		raise InvalidSyntaxError(0,"toUni","toUni takes only 1 argument")

funcDefiner = {
	"show":    func1,
	"add":     func2,
	"input":   func3,
	"toString":func4,
	"toInt":   func5,
	"sub":     func6,
	"mul":     func7,
	"div":     func8,
	"toChar":  func9,
	"toUni":   func10
}
