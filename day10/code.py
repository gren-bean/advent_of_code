"""
Advent of Code Problem 10

See Readme for details

"""
import numpy as np

class solver():

	graph = {}
	paths_to_goal_count = {}

	def __init__(self, data, verbose=0):
		self.verbose = verbose
		
		end_val = max(data) + 3
		d = [0] + data + [end_val]
		d.sort()
		self.data = d
		self.num_adapters = len(d)


	def part1(self):
		data = np.array(self.data)
		diffs = np.diff(data)
		unique, counts = np.unique(diffs, return_counts=True)
		for i in range(len(unique)):
			print(f"Diff of {unique[i]} count: {counts[i]}")
		print(f"Counts multiplied: {np.prod(counts)}")


	def build_graph(self):
		"""
		Builds Directed Graph

		Adapters are nodes (including start node of 0 and ending value)
		Directed edges go from adapter => adapters they can plug into
		"""
		for u in range(self.num_adapters):
			# Add node to graph
			self.graph[self.data[u]] = []
			offset = 1
			diff = 0
			# Add neighbor nodes
			while self.num_adapters > u + offset:
				diff = self.data[u+offset] - self.data[u]
				if diff < 4:
					self.graph[self.data[u]].append(self.data[u+offset])
					offset += 1
				else:
					break

		# Debugging Output			
		if self.verbose >= 1:
			print("CONSTRUCTED GRAPH:")
			for u in self.graph:
				print(f"{u}: {self.graph[u]}")


	def explore(self, s, t):
		"""
		Simple DFS graph exploration starting from node s
		Searching for goal t

		O(|V|+|E|) complexity
		"""
		
		# Mark node visited
		self.visited[s] = True
			
		# Loop through all neighbors to node
		for v in self.graph[s]:
			# If node has not been visited, explore
			if self.visited[v] == False:
				self.explore(v, t)

			# Update paths to goal count
			self.paths_to_goal_count[s] += self.paths_to_goal_count[v]

			# Debugging output
			if self.verbose >= 1:
				print(f"Node {s} updated after neighbor {v}")
				print(f"Node {s} has {self.paths_to_goal_count} paths to goal now.\n")

		# Debugging output
		if self.verbose >= 1:
			print(f"DONE exploring {s}. {self.paths_to_goal_count[s]} paths to goal\n")

	def find_all_paths(self, start, goal):
		"""
		Finds all distinct paths from start node to goal node

		Assumes a directed graph
		"""
		# Initialize visited array
		self.visited = {}
		for u in self.graph: self.visited[u] = False

		# Set goal node to visited
		self.visited[goal] = True

		# Initialize paths to goal
		for u in self.graph: self.paths_to_goal_count[u] = 0
		self.paths_to_goal_count[goal] = 1

		# Run DFS
		self.explore(start, goal)
		print(f"Part2 Answer: Found {self.paths_to_goal_count[start]} paths to goal")
		

def read_input(filename, verbose=0):
	"""
	Read in Input

	Requires:
	- file to be in current working directory
	- each line to be an integer
	"""
	data = []
	with open(filename,"r") as f:
		lines = f.readlines()
		for line in lines:
			data.append(int(line.strip()))
	return data


def part1(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	s = solver(data, verbose=verbose)
	s.part1()
	

def part2(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	s = solver(data, verbose=verbose)
	s.build_graph()
	s.find_all_paths(0, 155)
		

def main(verbose=0):
	# part1(verbose=verbose)
	part2(verbose=verbose)

if __name__ == "__main__":
    main(verbose=0)