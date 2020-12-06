
"""
Advent of Code Problem 4

Part1: Binary Partitioning to find highest value seat
Part2: Find seat, only 'real' seat missing. Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.
"""
import re

def read_input(filename, verbose=0):
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
			data.append(line.strip())
	return data

def parse_input(data,verbose=0):
	parsed_data = {}
	for line in data:
		# Basic validation
		p1 = "(F|B){7}"
		p2 = "(R|L){3}"
		if re.match(p1,line[:7]) and re.match(p2,line[-3:]):
			str_bin = line.translate(line.maketrans('FBRL', '0110'))
			parsed_data[int(str_bin[:7],base=2) * 8 + int(str_bin[-3:],base=2)] = \
					{"seat":line,"row":int(str_bin[:7],base=2),"col":int(str_bin[-3:],base=2)}
			if verbose==1:
				print(f"\n{line} ==> {str_bin}")
				print({"seat":line,"row":int(str_bin[:7],base=2),"col":int(str_bin[-3:],base=2)})
	return parsed_data

def part1(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	parsed_data = parse_input(data,verbose=verbose)
	# Find highest number seat
	highest_seat_id = 0
	for p in parsed_data:
		highest_seat_id = max(p,highest_seat_id)
	print(highest_seat_id)
		
def part2(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	parsed_data = parse_input(data)
	
	# Find your seat
	ids = parsed_data.keys()
	ids = sorted(ids)
	for i in range(len(ids)-1):
		if (ids[i] + 1) != ids[i+1] and ids[i+1] == (ids[i] + 2):
			print(f"Missing seat ID: {ids[i]+1}")

def main(verbose=0):
	part1(verbose=verbose)
	part2(verbose=verbose)

if __name__ == "__main__":
    main(verbose=0)