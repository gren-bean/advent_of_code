"""
Advent of Code Problem 13

See Readme for details

"""
import math

class solver():
    """
    Solves the problem
    """

    def __init__(self, part, data, verbose=0):
        self.verbose = verbose
        self.part = part  # Part of the problem to solve: [1 or 2]
        self.earliest = int(data[0])
        tmp = data[1].split(',')
        self.bus_schedule = []
        self.bus_sequence = {}
        for i in range(len(tmp)):
            if tmp[i] != "x": 
                self.bus_sequence[i] = int(tmp[i])
                self.bus_schedule.append(int(tmp[i]))


    def find_bus(self):
        """Find first bus to arrive after 'earliest' timestamp"""
        bus_id = 0
        offset = -1
        run = True
        while run:
            offset += 1
            for route_time in self.bus_schedule:
                if (self.earliest + offset) % route_time == 0:
                    bus_id = route_time
                    run = False
                    break
        print(f"Earliest Bus: {bus_id}")    
        print(f"Waiting for: {offset} mins")
        print(f"Product of above two numbers: {bus_id*offset}")


    def extended_euclidean(a, b): 
        """Extended Euclid function"""
        if a == 0: 
            return (b, 0, 1) 
        else: 
            g, y, x = extended_euclidean(b % a, a) 
            return (g, x - (b // a) * y, y) 
      
 
    def modinv(a, n): 
        """Finds modular inverse"""
        g, x, y = extended_euclidean(a, n) 
        return x % n 


    def find_magic_timestamp(self):
        """Find first timestamp with a buses arriving in desired
        sequence. Uses Chinese Remainder Theorem Direct Construction"""
        curr_time = self.bus_sequence[0]
        run = True
        print(self.bus_sequence)
        ids = []
        fullProduct = 1
        for i in range(len(data[1])):
            item = data[1][i]
            if item != 'x':
                k = int(item)
                i = i % k
                ids.append(((k-i)%k,k))
                fullProduct *= k

        total = 0
        for i,k in ids:
            partialProduct = fullProduct // k

            inverse = mod_inverse(partialProduct,k)
            assert (inverse * partialProduct) % k == 1

            term = inverse * partialProduct * i
            total += term

        return total % fullProduct


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


def part1(verbose=0):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    s = solver(1, data, verbose=verbose)
    s.find_bus()


def part2(verbose=0):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)      
    s = solver(2, data, verbose=verbose)
    s.find_magic_timestamp()    

def main(verbose=0):
    # part1(verbose=verbose)
    part2(verbose=verbose)

if __name__ == "__main__":
    main(verbose=0)