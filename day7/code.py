
"""
Advent of Code Problem 7

Part1: You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold bag?)

Part2: not yet started

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
	bid = 0  # bag id
	return parsed_data

def part1(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	parsed_data = parse_input(data,verbose=verbose)
	
		
def part2(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	parsed_data = parse_input(data)	

def main(verbose=0):
	part1(verbose=verbose)
	part2(verbose=verbose)

if __name__ == "__main__":
    main(verbose=0)