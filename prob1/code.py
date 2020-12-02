
"""
Advent of Code Problem 1

Specifically, they need you to find the two entries that sum to 2020 and 
then multiply those two numbers together.

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

def main(verbose=False):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	# Assumes positive integers only
	answer = None
	for i in range(len(data)):
		for j in range(len(data)):
			for k in range(len(data)):
				if k not in [i,j] and data[i] + data[j] + data[k] == 2020:
					answer = data[i] * data[j] * data[k]
					print(f"Answer is {answer}. ({data[i]} + {data[j]} + {data[k]} = 2020)")
					return
		
	print("ERROR: No 2 numbers sum to 2020!")

if __name__ == "__main__":
    main(verbose=False)