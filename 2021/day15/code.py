"""
Advent of Code 2021 Problem X

Part1: TBD
Part2: TBD
"""

def read_input(filename, verbose=False):
	"""
	Read in Input

	Requires:
	- file to be in current working directory
	"""	
	data = []
	with open(filename,"r") as f:
		lines = f.readlines()
	# Process input
	for line in lines:
		data.append(line)
	return data


def part1(verbose=False):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	# Do stuff
	pass


def part2(verbose=False):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	# Do stuff
	pass


if __name__ == "__main__":
    part1(verbose=False)
    part2(verbose=False)