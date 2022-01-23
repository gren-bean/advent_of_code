"""
Advent of Code 2021 Problem 14

Part1: Grow polymer chain and count most and least common elements in the result
Part2: TBD
"""

from collections import Counter

def read_input(filename, verbose=False):
    """
    Read in Input and Process
    """
    data = []
    with open(filename,"r") as f:
        for line in f.readlines():
            data.append(line.strip())

    return data


class polymer_chain():

    def __init__(self, polymer, data):
        """Initializes polymer template object"""

        self.p_string = polymer  # Initialize polymer chain (str)
        self.rules = {}  # Contains rules for character pairs
        
        # Populate rules
        for d in data:
            new_rule = d.split('->')
            self.rules[new_rule[0].strip()] = new_rule[1].strip()


    def __str__(self):
        """Returns string representation"""
        output = ""
        counts = Counter(self.p_string)
        counts_sorted = counts.most_common()
        mc = counts_sorted[0][1]
        lc = counts_sorted[-1][1]
        output += f'Length: {len(self.p_string)}\n'
        for item in counts_sorted: output += f'\t{item}\n'
        output += f'\tdiff b/w most & least common: {mc - lc}\n'
        return output


    def step(self):
        """Grows polymer template by one step"""
        new_string = self.p_string[0]
        for i in range(len(self.p_string) - 1):
            new_string += self.rules[self.p_string[i:i+2]]\
                        + self.p_string[i+1]
        self.p_string = new_string


    def grow_chain(self, N):
        """Grows polymer chain 'N' steps"""
        for i in range(N):
            self.step()



def solution(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    
    pc1 = polymer_chain(data[0], data[2:])
    pc1.grow_chain(10)
    print('Part 1:')
    print(pc1)
    # print('='*50 + '\nPart 2:')
    # pc2 = polymer_chain(data[0], data[2:])
    # pc2.grow_chain(40)
    # print(pc2)


if __name__ == "__main__":
    solution(verbose=False)