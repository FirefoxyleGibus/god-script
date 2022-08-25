from engine.instructions.instruction import *

class CondInstruction(Instruction):   # parsing conditionnal stuff
	def __init__(self, instruction_str, filepos):
		Instruction.__init__(self, instruction_str, filepos)

		parts    = []
		self.ops = []
		cur, op = "", ""
		for c in self.str:
			if c in "&|":
				if len(op) == 0: # got one part
					parts.append(cur)
					cur = "" # reset
				op += c
				if len(op) == 2: # end of operator
					self.ops.append(op)
					op = "" # reset
				continue
			cur += c
		parts.append(cur)

		self.parts = []
		for part in parts:
			left, right, op = "", "", ""
			for c in part:
				if c in "!=<>":
					op+=c
					continue
				# get both side of cond
				if len(op) != 2: left  += c
				else:            right += c
			print((left.rstrip().lstrip(), op, right.rstrip().lstrip()))
			self.parts.append((left, op, right))

	def _parse_side(self, side_str, registry):
		t = Variable.get_type(side_str)
		if t == GSC_TYPES["STR"]:
			return registry.get_var(side_str.rstrip().lstrip())
		else:
			return Variable.parse_to_type(side_str)

	def exec(self, registry):
		res = False
		for i, part in enumerate(self.parts):
			left, op, right = part
			l = self._parse_side(left,  registry)
			r = self._parse_side(right, registry)
			part_res = 0
			if op == "==":   part_res = l == r
			elif op == "!=": part_res = l != r
			elif op == "<=": part_res = l <= r
			elif op == ">=": part_res = l >= r
			else:            part_res = False
			print(i, part_res)

			if i >= 1:
				cond_op = self.ops[i - 1]
				if cond_op == "&&": res = res and part_res
				if cond_op == "||": res = res or part_res
			else:
				res = part_res
		return res