"""
Advent of Code 2021 Problem X

Part1: Find final position of submarine, then multiple horizontal by vertical.
Part2: Same as part 1, but now submarine rotates vise simple x-y motion
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
	dt = {
		'forward':(1,0),
		'up':(0,-1),  # decreases depth
		'down':(0,1)
	}
	for line in lines:
		command = line.split(' ')
		cmd = command[0]
		val = int(command[1])
		data.append((val * dt[cmd][0],val * dt[cmd][1]))
	return data


def part1(verbose=False):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	pos = [0,0]  # represents x,y
	for d in data:
		# Update horizontal
		pos[0] += d[0]
		# Update vertical - max is zero (submarines can't fly)
		pos[1] = max((pos[1] + d[1],0))
	print(f"Final pos: {pos}, answer = {pos[0]*pos[1]}")


def part2(verbose=False):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	# Do stuff
	pos = [0,0,0]  # represents [x, y, direction]
	for d in data: # d = [forward move, aim change]
		# Update horizontal
		if d[0] > 0:
			pos[0] += d[0]
			pos[1] += d[0] * pos[2]
		else:
			pos[2] += d[1]  # update aim
	print(f"Final pos: {pos}, answer = {pos[0]*pos[1]}")	


if __name__ == "__main__":
    part1(verbose=False)
    part2(verbose=False)