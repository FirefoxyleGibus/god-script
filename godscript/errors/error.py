class Error(Exception):
	def __init__(self) -> None:
		pass

	def __str__(self) -> str:
		return "Error"

	def __repr__(self) -> str:
		return "Error("+self.__class__.__name__+")"