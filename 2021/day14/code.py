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

    def __init__(self, polymer, data, verbose=False):
        """Initializes polymer template object"""
        self.verbose = verbose

        # build polymer graph
        self.p_graph = {}
        self.p_start = polymer[0] # First letter
        self.p_end = polymer[-1]  # Last letter
          
        # Build polymer graph
        chars = []  
        for d in data:
            rule = d.split('->')
            pair = rule[0].strip()
            c = rule[1].strip()
            self.p_graph[pair] = {
                'chars': (pair[0], pair[1]),
                'nbrs': (pair[0] + c, c + pair[1]),
                'val': 0
            }
            # Update list of all letters
            chars += [pair[0], pair[1]]

        # Build list of all unique letters
        self.unique_chars = list(set(chars))

        # Initialize starting pairs
        for i in range(len(polymer) - 1):
            self.p_graph[polymer[i:i+2]]['val'] += 1


    def __str__(self):
        """Returns string representation"""
        output = "Letter Counts:\n"
        if self.verbose:
            for p in self.p_graph:
                output += f"/t{p}: {self.p_graph[p]['val']}\n"
            output += "\n"

        # Initialize letter counts
        l_counts = {}  
        for c in self.unique_chars: l_counts[c] = 0

        # Update letter counts based on number of each pair
        # Each letter can only appear in two pairs
        for p in self.p_graph:
            for c in self.p_graph[p]['chars']:
                l_counts[c] += self.p_graph[p]['val']

        # Divide by two to account for each letter appearing in two pairs
        # Also add 1 for first and last letter
        for c in l_counts:
            l_counts[c] = l_counts[c] // 2
            if c == self.p_start: l_counts[c] += 1
            if c == self.p_end: l_counts[c] += 1

        # Sort
        l_counts_list = sorted(l_counts.items(), key=lambda x:x[1])
        mc = l_counts_list[-1][1]  # most common count
        lc = l_counts_list[0][1]   # least common count
        for c in l_counts_list:
            output += f"\t{c[0]}: {c[1]}\n"
        
        output += f'\tdiff b/w most & least common: {mc - lc}\n'
        return output


    def step(self):
        """Grows polymer template by one step"""
        prev = {}
        # Save of previous and reset polymer graph
        for p in self.p_graph:
            prev[p] = self.p_graph[p]['val']
            self.p_graph[p]['val'] = 0

        for p in prev:
            if prev[p] > 0:
                # Every node has exactly two neighbors
                self.p_graph[self.p_graph[p]['nbrs'][0]]['val'] += prev[p]
                self.p_graph[self.p_graph[p]['nbrs'][1]]['val'] += prev[p]


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
    print('='*50 + '\nPart 2:')
    pc2 = polymer_chain(data[0], data[2:])
    pc2.grow_chain(40)
    print(pc2)


if __name__ == "__main__":
    solution(verbose=False)