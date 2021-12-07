"""
Advent of Code 2021 Problem X

Part1: Most common digit by column
Part2: TBD
"""

from collections import Counter

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
		data.append(list(line.strip()))
	return data


def part1(verbose=False):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	# Data is a 2d array of chars
	# Loop over columns
	height = len(data)
	gb = ""  # gamma
	eb = ""  # epsilon
	for i in range(len(data[0])):
		total = sum([ int(d[i]) for d in data ])
		if total > height/2: 
			gb += '1'
			eb += '0'
		else: 
			gb += '0'
			eb += '1'
	gd = int(gb,2)
	ed = int(eb,2)
	print(f"Gamma binary: {gb} | dec: {gd}")
	print(f"Epsilon binary: {eb} | dec: {ed}")
	print(f"Power consumption: {gd*ed}")



def part2(verbose=False):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	# data = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
	# Data is a 2d array of chars
	data_oxy = data.copy()
	data_co2 = data.copy()

	# Oxygen rating
	for i in range(len(data[0])): # Move through columns
		half_height = len(data_oxy) / 2
		# Most significant bit
		msb = '0'
		if sum([int(d[i]) for d in data_oxy]) >= half_height:
			msb = '1'

		# Reduce search space
		data_oxy = [ d for d in data_oxy if d[i] == msb ]

		# Check for search conclusion
		if len(data_oxy) == 1:
			break
	
	# CO2 rating
	for i in range(len(data[0])): # Move through columns
		half_height = len(data_co2) / 2
		# Least significant bit
		lsb = '1'
		if sum([int(d[i]) for d in data_co2]) >= half_height:
			lsb = '0'
		
		# Reduce search space
		data_co2 = [ d for d in data_co2 if d[i] == lsb ]
		
		# Check for search conclusion 
		if len(data_co2) == 1:
			break

	oxy_rating = int(''.join(data_oxy[0]),2)
	co2_rating = int(''.join(data_co2[0]),2)
	print(f"Life Support = Oxy * C02 = {oxy_rating} * {co2_rating} = {oxy_rating*co2_rating}")


if __name__ == "__main__":
    part1(verbose=False)
    part2(verbose=False)