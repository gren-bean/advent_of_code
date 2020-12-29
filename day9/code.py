
"""
Advent of Code Problem 9

Part1: Find first invalid number in the cipher.

Part2: Contiguous subset of at least 2 numbers that sum to number from step 1

"""


class custom_cipher():

	def __init__(self, data, verbose=0):
		self.verbose = verbose
		self.N = 25
		self.data = data
		self.subset = set(self.data[:self.N]) # Subset, each val points to index of next item
		self.offset = 0

		# Preamble
		if verbose >=1:
			print(f"Preamble: {self.subset}")

	def twosum(self, subset, val):
		"""Solves TwoSum, assuming subset is a hashmap"""
		for i in subset:
			if (val - i) in subset:
				return True
		return False


	def first_invalid_num(self):
		for d in self.data[self.N:]:
			if self.twosum(self.subset, d):
				if self.verbose >= 2:
					print(f"{d} has valid sum in subset {self.subset}")
				
				# Update subset
				self.subset.remove(self.data[self.offset])  # Remove earliest element
				self.subset.add(self.data[self.offset + self.N])  # add next element
				self.offset += 1  # incrememnt offset
			else:
				if self.verbose >= 1:
					print(f"{d} does NOT have valid sum in subset {self.subset}")
				self.target_num = d
				return d
		print("NO INVALID NUMBER FOUND")
		return 0

	def find_weakness(self):
		# Throw out all numbers too large
		filtered = [i for i in self.data if i < self.target_num]

		# Sliding window approach
		lower_bound = 0
		upper_bound = 1
		while 1:
			s = sum(filtered[lower_bound:upper_bound])
			if s < self.target_num:
				upper_bound += 1
			elif s > self.target_num:
				lower_bound += 1
			else:
				print(f"Found Contiguous Subsequence Summing to {self.target_num}!")
				print(f"\t{filtered[lower_bound:upper_bound]}")
				answer = min(filtered[lower_bound:upper_bound]) + max(filtered[lower_bound:upper_bound])
				print(f"\tSum of min & max elements in subsequence: {answer}")
				break
			if lower_bound >= upper_bound:
				print(f"ERROR: Bounds intersection at {lower_bound}")


def read_input(filename, verbose=0):
	"""
	Read in Input

	Requires:
	- file to be in current working directory
	- each line to be an integer
	"""
	data = []
	with open(filename,"r") as f:
		lines = f.readlines()
		for line in lines:
			data.append(int(line.strip()))
	return data

def part1(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	cp = custom_cipher(data, verbose=verbose)
	cp.first_invalid_num()
		
def part2(verbose=0):
	input_file = "input.txt"
	data = read_input(input_file, verbose=verbose)
	cp = custom_cipher(data, verbose=verbose)
	cp.first_invalid_num()
	cp.find_weakness()

def main(verbose=0):
	# part1(verbose=verbose)
	part2(verbose=verbose)

if __name__ == "__main__":
    main(verbose=1)