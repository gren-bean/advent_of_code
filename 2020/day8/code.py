
"""
Advent of Code Problem 8

Part1: Find accumulator value before instruction sequence loops

Part2: Identify single NOP or JMP instruction that will allow 
program to complete. Identify accumulator value after this is fixed.

"""

class custom_program():

	program = {}
	end = 0
	accumulator = 0
	ops_in_loop = []  # Only nop and jmp ops
	ops_to_end = []

	def __init__(self, data, verbose=0):
		# Read in code
		for i in range(len(data)):
			if len(data[i]) < 1: continue  # Skip empty lines
			instr = data[i].split(" ")
			op_type = instr[0]
			val = int(instr[1])
			# Determine next instruction. Can't be less than zero.
			next_op = i+1
			if op_type == "jmp": 
				next_op = max(0,i+val)
			self.program[i] = {"type":op_type,"val":val,"next":next_op,"visited":0}
		self.end = len(self.program)

	def run_program(self):
		self.accumulator = 0
		for p in self.program:
			self.program[p]["visited"] = 0
		
		instr = 0
		visited = 0
		# Run program to end, 
		# Identify and break if an infinite loop is discovered
		while visited == 0:
			self.program[instr]["visited"] = 1
			op_type = self.program[instr]["type"]
			val = self.program[instr]["val"]
			if op_type == "acc": 
				# Accumulator can't go below zero
				self.accumulator = max(0,self.accumulator+val)
			else:
				# Book-keeping of ops in loop
				self.ops_in_loop.append(instr)
			instr = self.program[instr]["next"]
			# Check if program has ended
			if instr == self.end: break
			# Updated visited flag
			visited = self.program[instr]["visited"]
		# Return final accumulator value
		return self.accumulator

	def build_rev_graph(self):
		self.Rgraph = {}
		# Build empty adjacency list
		# Use -1 to indicate no predecessor
		for i in range(self.end): 
			self.Rgraph[i] = {}
		# Build reverse graph in adjacency list form
		for op in self.program:
			if self.program[op]["next"] >= self.end: continue
			self.Rgraph[self.program[op]["next"]][op] = 1

	def explore_reverse_graph(self, start_node):
		"""
		DFS graph exploration from start_node
		O(|V|+|E|) complexity
		"""
		self.ops_to_end.append(start_node)
		self.visited[start_node] = True
		for v in self.Rgraph[start_node]:
			if self.visited[v] == False:
				self.explore_reverse_graph(v)

	def dfs_reverse_graph(self,start_node):
		"""
		DFS on Reversed Graph
		"""
		
		# Initialize visited flag to false
		self.visited = {}
		for v in self.Rgraph:
			self.visited[v] = False
		return self.explore_reverse_graph(start_node)

	def fix_program(self):
		"""
		Find the single NOP or JMP that lets program run to end

		We know it must be one of the ones in the initial loop.
		Need to connect it to an op that leads to end.
		"""

		# Find all ops that will allow program completion
		r = self.run_program()
		self.build_rev_graph()
		self.dfs_reverse_graph(self.end-1)
		
		# Determine which NOP or JMP is corrupted
		for op in self.ops_in_loop:
			if self.program[op]["type"] == "jmp" and (op + 1) in self.ops_to_end:
				print(f"Updating this instruction from JMP to NOP to fix program:")
				print(f"\t#{op} OLD: {self.program[op]}")
				self.program[op]["type"] = "nop"
				self.program[op]["next"] = op+1
				print(f"\t#{op} NEW: {self.program[op]}")
				break
			elif (op + self.program[op]["val"]) in self.ops_to_end:
				print(f"Updating this instruction from NOP to JMP to fix program:")
				print(f"\t#{op} OLD: {self.program[op]}")
				self.program[op]["type"] = "jmp"
				self.program[op]["next"] = max(0,op + self.program[op]["val"])
				print(f"\t#{op} NEW: {self.program[op]}")
				break

		# Run corrected program
		r = self.run_program()
		return r


def read_input(filename, verbose=0):
	"""
	Read in Input

	Requires:
	- file to be in current working directory
	"""
	data = []
	with open(filename,"r") as f:
		lines = f.readlines()
		for line in lines:
			data.append(line.strip())
	return data

def part1(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	cp = custom_program(data)
	answer = cp.run_program()
	print(f"Part1 answer: {answer}")
		
def part2(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	cp = custom_program(data)
	answer = cp.fix_program()
	print(f"Part1 answer: {answer}")

def main(verbose=0):
	part1(verbose=verbose)
	part2(verbose=verbose)

if __name__ == "__main__":
    main(verbose=0)