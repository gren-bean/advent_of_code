"""
Advent of Code 2021 Problem 1

Part1: Count number of times measurement increases
Part2: Count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.
"""

def read_input(filename, verbose=False):
	"""
	Read in Input

	Requires:
	- file to be in current working directory
	- each line of input file to be an integer without whitespace
	"""	
	data = []
	with open(filename,"r") as f:
		lines = f.readlines()
	for line in lines:
		try:
			num = int(line.strip())
			data.append(num)
		except:  # Not an integer
			continue
		if verbose:
			print(num)
	return data


def part1(verbose=False):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	cnt = 0
	for i in range(len(data[1:]) + 1):
		if data[i] > data[i-1]:
			cnt +=1
	print(f"Solution: {cnt}")


def part2(verbose=False):
	

if __name__ == "__main__":
    part1(verbose=False)