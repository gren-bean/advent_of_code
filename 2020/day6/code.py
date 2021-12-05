
"""
Advent of Code Problem 6

Part1: Sum of unique questions for each group answered yes.
Part2: Sum of questions for each group everyone answered yes.
"""
import re

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

def parse_input(data,verbose=0):
	parsed_data = {}
	gid = 0  # group id
	parsed_data[gid] = {'answers':"",'num_people':0}
	for line in data:
		# Blank line, start new group
		if len(line) < 1:
			gid += 1
			parsed_data[gid] = {'answers':"",'num_people':0}
		else:
			parsed_data[gid]['answers'] += line.strip()
			parsed_data[gid]["num_people"] += 1
	return parsed_data

def part1(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	parsed_data = parse_input(data,verbose=verbose)
	# Find sum of counts of unique "yes" questions
	sum_of_yes = 0
	for gid in parsed_data:
		# Collapses string to only unique letters
		sum_of_yes += len(''.join(set(parsed_data[gid]["answers"])))
	print(f"Sum of unique YES answers for each grouip: {sum_of_yes}")
		
def part2(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	parsed_data = parse_input(data)
	sum_of_all_yes = 0
	# Find sum of counts of "yes" questions everyone answered
	for gid in parsed_data:
		unique_answers = ''.join(set(parsed_data[gid]["answers"]))
		for c in unique_answers: 
			if parsed_data[gid]["answers"].count(c) == parsed_data[gid]["num_people"]:
				sum_of_all_yes +=1
	print(f"Sum of answers ALL members of group answered YES to: {sum_of_all_yes}")
		

def main(verbose=0):
	part1(verbose=verbose)
	part2(verbose=verbose)

if __name__ == "__main__":
    main(verbose=0)