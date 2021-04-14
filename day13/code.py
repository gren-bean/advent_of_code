"""
Advent of Code Problem 13

See Readme for details

"""
import math

def compute_lcm(a):
    """Computes least common multiple"""
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm

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
        self.bus_sequence = []
        self.last_bus_min=len(tmp)
        for i in range(len(tmp)):
            if tmp[i] != "x": 
                self.bus_sequence.append((i,int(tmp[i])))
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
        
        print(f"Bus Sequence: {self.bus_sequence}")
        # Start at timestamp zerp
        timestamp = 0
        matched_buses = [self.bus_sequence[0][1]]
        while True:
            # Minimizes search space by jumping distances of least common multiples
            timestamp += compute_lcm(matched_buses)
            print(f"Current Timestamp: {timestamp}")
            for arrival_min, bus_id in self.bus_sequence:
                if (timestamp + arrival_min) % bus_id == 0:
                    if bus_id not in matched_buses:
                        matched_buses.append(bus_id)
            if len(matched_buses) == len(self.bus_sequence):
                break

        return timestamp


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
    r = s.find_magic_timestamp()
    print(f"Solution to part 2 is time: {r}")


def main(verbose=0):
    # part1(verbose=verbose)
    part2(verbose=verbose)

if __name__ == "__main__":
    main(verbose=0)