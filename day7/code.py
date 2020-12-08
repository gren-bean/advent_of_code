
"""
Advent of Code Problem 7

Part1: You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

Part2: not yet started

"""
import string, re

class color_graph():

	verbosity=0
	graph={}  # Dict of lists representing directed graph
	visited={}  # Tracking for Graph Search
	color_match = re.compile("[a-z]+\s[a-z]+")

	def __init__(self, data, verbose=0):
		self.verbosity = verbose
		cc = 0  # color codes
		exclude = ["bag","bags","contain","no","other"]
		for line in data:
			# Split on any non-alphanumeric character and remove unwanted words
			line = [word for word in re.split("\W+",line) if word not in exclude]
			line = ' '.join(line)
			colors = re.findall(self.color_match,line)
			parent = colors[0]
			if parent in self.graph:
				self.graph[parent] += colors[1:]
			else:
				self.graph[parent] = []
				self.graph[parent] += colors[1:] 
		# Debug Output
		if self.verbosity >= 2:
			for d in self.graph:
				print(f"{d} - {self.graph[d]}")

	def explore(self, v, goal):
		"""
		Subroutine of DFS, runs explore from node v
		"""
		self.visited[v] = True
		for u in self.graph[v]:
			if u == goal:
				return True
			if self.visited[u] == False: 
				if self.explore(u,goal) == True: return True
		return False

	def dfs(self, goal):
		"""
		Runs DFS search from every source node to determine 
		number of paths to dest
		"""
		paths_to_goal = 0
		# Loop through all start nodes
		for v in self.graph:
			# First set every node's visited value to false
			for u in self.graph:
				self.visited[u] = False
			# Explore starting from this node
			if self.explore(v, goal) == True:
				paths_to_goal += 1
		return paths_to_goal
			

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
	graph = color_graph(data,verbose=verbose)
	answer = graph.dfs("shiny gold")
	print(f"Ways to store Shing Gold Bag: {answer}")
		
def part2(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	parsed_data = color_graph(data)	

def main(verbose=0):
	part1(verbose=verbose)
	# part2(verbose=verbose)

if __name__ == "__main__":
    main(verbose=0)