
"""
Advent of Code Problem 3

Part1: How many trees are in your path
Part2: Product of trees in path for 5 different sled routes

"""
import math

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

def count_trees(data, x_step, y_step):
	x=0
	y=0
	height = len(data)
	width = len(data[0])
	tree_count = 0
	if data[0][0] == '#': tree_count += 1
	while y < height-1:
		y += y_step
		x = (x + x_step) % width
		if data[y][x] == '#': tree_count += 1
	return tree_count

def part1(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	tree_count = count_trees(data, 3, 1)
	print(f"{tree_count} trees on part1")
		
def part2(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	runs = [{"x_step":1,"y_step":1},
	{"x_step":3,"y_step":1},
	{"x_step":5,"y_step":1},
	{"x_step":7,"y_step":1},
	{"x_step":1,"y_step":2}]
	tree_counts = []
	for r in runs:
		tree_counts.append(count_trees(data, r["x_step"], r["y_step"]))
	print(f"Answer: {math.prod(tree_counts)}")

def main(verbose=0):
	part1(verbose=verbose)
	part2(verbose=verbose)

if __name__ == "__main__":
    main(verbose=1)
