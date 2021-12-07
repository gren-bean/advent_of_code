"""
Advent of Code 2021 Problem 1

Part1: Count number of times measurement increases
Part2: Count the number of times the sum of measurements in this (N=3)sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.
"""

def calc_moving_sum(data, window_size=3):
	"""
	Helper function - calculates moving sum for list of integers

	Looks ahead until window_size measurements are captured in the sum is
	reached
	"""
	moving_sums = []
	if window_size > len(data):
		print("ERROR: window_size larger than dataset.")
	for i in range(len(data) - window_size + 1):
		moving_sum = sum(data[i: i + window_size])
		moving_sums.append(moving_sum)
		print(moving_sum)
	return moving_sums


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
	"""
	Identify increase in measurement from prev
	"""
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	cnt = 0
	for i in range(len(data[1:]) + 1):
		if data[i] > data[i-1]:
			cnt +=1
	print(f"Solution: {cnt}")


def part2(verbose=False):
	"""
	Identify increase in moving 3-measurement average
	"""
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	# data = [199,200,208,210,200,207,240,269,260,263]  # test data

	# Get moving sums
	moving_sums = calc_moving_sum(data)
	# Same process as before
	cnt = 0
	for i in range(len(moving_sums[1:]) + 1):
		if moving_sums[i] > moving_sums[i-1]:
			cnt +=1
	print(f"Solution: {cnt}")	



if __name__ == "__main__":
    part1(verbose=False)
    part2(verbose=False)