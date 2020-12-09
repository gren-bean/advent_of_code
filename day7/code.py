
"""
Advent of Code Problem 7

Part1: You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

Part2: not yet started

"""
import string, re

class color_graph():

	verbosity=0
	graph={}  # Dict of lists representing directed graph
	Rgraph={} # Reversed graph
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
			# Find colors and corresponding number
			colors = re.findall(self.color_match,line)
			bag_nums = re.findall("[0-9]+",line)
			# Parent Node
			parent_color = colors[0]
			child_colors = colors[1:]
			# Add to graph
			if parent_color in self.graph:
				for i in range(len(child_colors)):
					self.graph[parent_color][child_colors[i]] = int(bag_nums[i])
			else:
				self.graph[parent_color] = {} # In case of no children
				for i in range(len(child_colors)):
					self.graph[parent_color][child_colors[i]] = int(bag_nums[i])
		# Debug Output
		if self.verbosity >= 2:
			for d in self.graph:
				print(f"{d} - {self.graph[d]}")

	def explore_reverse_graph(self, start_node):
		"""
		Simple DFS graph exploration starting from node v
		O(|V|+|E|) complexity
		"""
		self.visited[start_node] = True
		visited_nodes = 1
		for v in self.Rgraph[start_node]:
			if self.visited[v] == False: 
				visited_nodes += self.explore_reverse_graph(v)
		return visited_nodes

	def dfs_reverse_graph(self,start_node):
		# Initialize 'visited variable'
		visited_nodes = 1
		for v in self.Rgraph:
			self.visited[v] = False
			for u in self.Rgraph[v]: 
				self.visited[u] = False

		return self.explore_reverse_graph(start_node)

	def reverse_graph(self):
		"""
		Creates a reverse graph
		"""
		# Create reverse graph framework
		for v in self.graph:
			self.Rgraph[v] = {}
			for u in self.graph[v]:
				self.Rgraph[u] = {}

		# Fill in reverse graph
		for v in self.graph:
			for u in self.graph[v]:
				self.Rgraph[u][v] = self.graph[v][u]

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
	graph.reverse_graph()
	answer = graph.dfs_reverse_graph("shiny gold") - 1
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