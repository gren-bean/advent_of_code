
"""
Advent of Code Problem 4

Part1: Passwords with required fields ("cid" optional)
Part2: Each field meets below requirements
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.

"""
import math
import re

def print_passport(pp_dict):
	print(f"byr:{pp_dict['byr']}")
	print(f"iyr:{pp_dict['iyr']}")
	print(f"eyr:{pp_dict['eyr']}")
	print(f"hgt:{pp_dict['hgt']}")
	print(f"hcl:{pp_dict['hcl']}")
	print(f"ecl:{pp_dict['ecl']}")
	print(f"pid:{pp_dict['pid']}")
	c = "no"
	if "cid" in pp_dict:c = "yes"
	print(f"cid:{c}")
	print(" ")

def check_byr(byr):
	"""Return True if valid birth year"""
	if len(byr) < 4: return False
	try:
		byr_ = int(byr)
		if 1920 <= byr_ <= 2002:
			return True
	except:
		pass
	return False

def check_iyr(iyr):
	"""Return True if valid issue year"""
	if len(iyr) < 4: return False
	try:
		iyr_ = int(iyr)
		if 2010 <= iyr_ <= 2020:
			return True  
	except:
		pass
	return False

def check_eyr(eyr):
	"""Return True if valid expiration year"""
	if len(eyr) < 4: return False
	try:
		eyr_ = int(eyr)
		if 2020 <= eyr_ <= 2030:
			return True
	except:
		pass
	return False	

def check_hgt(hgt):
	try:
		pattern ="[0-9]{2,3}(in|cm)"
		if re.match(pattern,hgt):
			if hgt[-2:] == "in":
				val = int(hgt[:2])
				if val >= 59 and val <= 76:
					return True
			if hgt[-2:] == "cm":
				val = int(hgt[:3])
				if val >= 150 and val <= 193:
					return True
	except:
		pass
	return False

def check_hcl(hcl):
	pattern = "#([0-9]|[a-f]){6}"
	if re.match(pattern,hcl):
		return True
	return False

def check_ecl(ecl):
	t = ["amb","blu","brn","gry","grn","hzl","oth"]
	if ecl in t:
		return True
	return False

def check_pid(pid):
	pattern = "[0-9]{9}"
	if re.match(pattern,pid) and len(pid) == 9:
		return True
	return False	

def check_field(key,value):
	if key == "byr":
		return check_byr(value)
	elif key == "iyr":
		return check_iyr(value)
	elif key == "eyr":
		return check_eyr(value)
	elif key == "hgt":
		return check_hgt(value)
	elif key == "hcl":
		return check_hcl(value)
	elif key == "ecl":
		return check_ecl(value)
	elif key == "pid":
		return check_pid(value)
	elif key == "cid":
		return True
	else:
		print(f"ERROR: Unexpected key-value pair - ({key},{value})")
		return False

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

def parse_input(data):
	parsed_data = {}
	unique_id = 0
	parsed_data[unique_id] = {}
	for line in data:
		# Start new passport
		if len(line) < 3:
			unique_id += 1
			parsed_data[unique_id] = {}
		else:
			entries = line.split(' ')
			for e in entries:
				kv = e.split(':') 
				parsed_data[unique_id][kv[0]] = kv[1]
	# Debug printing
	# for d in parsed_data: print(parsed_data[d])
	return parsed_data

def check_fields(data):
	passport_count = 0
	fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
	print()
	for d in data:
		# Because each entry is a dictionary, no duplicate keys
		keys = data[d].keys()
		if len(keys) == 8 or (len(keys) == 7 and "cid" not in keys):
			valid = True
			for k in keys:
				if k not in fields:
					valid = False
					# print(f"Invalid key found: {k}")
					break
			if valid: passport_count += 1
		# else:
		# 	print(f"\nInvalid passport:")
		# 	for k in data[d]:
		# 		print(f"{k}:{data[d][k]}")		
	return passport_count

def check_fields_strict(data,verbose=0):
	passport_count = 0
	fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
	print()
	for d in data:
		# Because each entry is a dictionary, no duplicate keys
		keys = data[d].keys()
		if len(keys) == 8 or (len(keys) == 7 and "cid" not in keys):
			check = all(item in fields for item in keys)
			if check:
				valid = True
				for k in keys:
					if check_field(k,data[d][k]) == False:
						# Debug
						if verbose == 1:
							print(f"INVALID FIELD: ({k}:{data[d][k]})\n")
						valid = False
						break
				if valid: 
					if verbose == 1:
						print_passport(data[d])
					passport_count += 1
	return passport_count

def part1(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	parsed_data = parse_input(data)
	valid_pp_count = check_fields(parsed_data)
	print(valid_pp_count)
		
def part2(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	parsed_data = parse_input(data)
	valid_pp_count = check_fields_strict(parsed_data,verbose=verbose)
	print(valid_pp_count)


def main(verbose=0):
	# part1(verbose=verbose)
	part2(verbose=verbose)

if __name__ == "__main__":
    main(verbose=1)