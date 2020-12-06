
"""
Advent of Code Problem 2

How many passwords are valid according to their policies?

"""

def read_input(filename, verbose=0):
	"""
	Read in Input

	Requires:
	- file to be in current working directory
	- expects each line to be in a certain format
		"<positive_digit>-<positive_digit> <letter>: <string>"
	"""
	
	data = {}
	with open(filename,"r") as f:
		lines = f.readlines()
		unique_id = 0 # To handle duplicate passwds
		for line in lines:
			# Strip leading/trailing whitespace
			line = line.strip().replace(':','')
			range_letter, letter, passwd = line.split(' ')
			min_letter, max_letter = range_letter.split('-')
			if not min_letter or not max_letter:
				continue
			data[unique_id] = {'passwd': passwd, 'letter':letter, 
								'min':int(min_letter), 'max':int(max_letter)}
			unique_id += 1
			if verbose >= 1:
				print(f"{min_letter}-{max_letter} {letter}: {passwd}")
	return data

def part1(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	raw_count = 0
	valid_passwds = 0
	for i in data:
		letter_count = data[i]['passwd'].count(f"{data[i]['letter']}")
		if letter_count >= data[i]['min'] and letter_count <= data[i]['max']:
			valid_passwds += 1
			if verbose >= 1:
				print(f"[{raw_count}] VALID password: {data[i]['passwd']} | {data[i]['letter']},{data[i]['min']}-{data[i]['max']}")
		elif verbose >= 1:
			print(f"[{raw_count}] NON-VALID password: {data[i]['passwd']} | {data[i]['letter']},{data[i]['min']}-{data[i]['max']}")
		raw_count += 1
	print(f"There were {valid_passwds} valid passwords in the input.")

def part2(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	raw_count = 0
	valid_passwds = 0
	for i in data:
		if (data[i]['passwd'][data[i]['min']-1] == data[i]['letter'])\
			and (data[i]['passwd'][data[i]['max']-1] != data[i]['letter']):
			valid_passwds += 1
			if verbose >= 1:
				print(f"[{raw_count}] VALID password: {data[i]['passwd']} | {data[i]['letter']},{data[i]['min']}-{data[i]['max']}")
		elif (data[i]['passwd'][data[i]['min']-1] != data[i]['letter'])\
			and (data[i]['passwd'][data[i]['max']-1] == data[i]['letter']):
			valid_passwds += 1
			if verbose >= 1:
				print(f"[{raw_count}] VALID password: {data[i]['passwd']} | {data[i]['letter']},{data[i]['min']}-{data[i]['max']}")
		elif verbose >= 1:
			print(f"[{raw_count}] NON-VALID password: {data[i]['passwd']} | {data[i]['letter']},{data[i]['min']}-{data[i]['max']}")
		raw_count += 1
	print(f"There were {valid_passwds} valid passwords in the input.")

def main(verbose=0):
	# part1(verbose=verbose)
	part2(verbose=verbose)

if __name__ == "__main__":
    main(verbose=1)
