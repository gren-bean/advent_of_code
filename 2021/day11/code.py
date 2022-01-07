"""
Advent of Code 2021 Problem 11

Part1: TBD
Part2: TBD
"""

class octopus_graph():
    """Represents an N x N octopus cave as a graph"""

    def __init__(self, data, size=10, cutoff=9, verbose=False):
        """
        Build cave
        
        :param data: (2-D list) Values of each octopus
        :param size: (int) N x N sized cave
        :param cutoff: (int) value that causes nodes to 'flash' and reset to zero
        :param verbose: (bool) turns on/off verbosity
        """
        self.verbose = verbose
        self.num_flashes = 0
        self.size = size
        self.cutoff = cutoff
        self.o_graph = {} # Octopus graph
        uid = 0
        for row in range(self.size):
            for col in range(self.size):
                # Build list of neighbors
                neighbors = []

                # Neighbors adjacent including diagonals
                for r in [-1, 0, 1]:
                    for c in [-1, 0, 1]:
                        # check boundaries, and skip the (0,0) case
                        if ((r,c) != (0,0)) and (0 <= (row + r) < self.size)\
                        and (0 <= (col + c) < self.size):
                            neighbors.append(uid + r*self.size + c)

                # Add node to graph
                self.o_graph[uid] = {
                    'w': int(data[row][col]),  # node weight
                    'nbrs': neighbors,  # neighbors
                    'flashed': False    # tracks if we've already flashed
                }

                # Increment uid
                uid += 1


    def __str__(self):
        """Return string representation of grid"""
        output = ''
        uid = 0
        for row in range(self.size):
            for col in range(self.size):
                output += str(self.o_graph[uid]['w'])
                uid += 1
            output += '\n'
        return output


    def str_zeros(self):
        """Return string representation of grid, with zeros only"""
        output = ''
        uid = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.o_graph[uid]['w'] == 0:
                    output += str(self.o_graph[uid]['w'])
                else:
                    output += '.'
                uid += 1
            output += '\n'
        return output


    def flash(self, s):
        """
        An adaption of BFS (breadth first search) to
        cause 'flashes' for nodes above cutoff value,
        and impact their neighboring nodes accordingly
        
        :param s: (int) starting node
        """
        Q = [s]
        while len(Q) > 0:
            u = Q.pop(0)
            for v in self.o_graph[u]['nbrs']:
                
                # Check node value
                if self.o_graph[v]['w'] <= self.cutoff:
                    # Increment node
                    self.o_graph[v]['w'] += 1

                    # If node is above cutoff and hasn't flashed,
                    # add to search
                    if self.o_graph[v]['w'] > self.cutoff and not self.o_graph[v]['flashed']:
                        Q.append(v)
                        self.o_graph[v]['flashed'] = True


    def make_step(self):
        """
        Runs a "time-step" where each octopus flashes,
        impacting neighbors

        :returns sync: (True/False) Whether all octopuses flashed or not
        """

        # Update energy level of every octopus by 1
        for u in self.o_graph:
            self.o_graph[u]['w'] += 1

        # For each node with weight > 9, run an expanding
        # Search to generate effects
        for u in self.o_graph:
            if self.o_graph[u]['w'] > self.cutoff and not self.o_graph[u]['flashed']:
                self.flash(u)

        # Mark octopuses that flashed back to zero!
        step_flashes = 0
        for u in self.o_graph:
            if self.o_graph[u]['w'] > self.cutoff:
                step_flashes += 1
                self.o_graph[u]['w'] = 0
                self.o_graph[u]['flashed'] = False
        self.num_flashes += step_flashes
        if step_flashes == (self.size * self.size):
            return True
        return False
        


def read_input(filename, verbose=False):
    """
    Read & Process in Input
    """ 
    data = []
    with open(filename,"r") as f:
        lines = f.readlines()

    # Process input
    for line in lines:
        data.append(line.strip())
    return data


def solution(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)

    g = octopus_graph(data)

    # Part1
    for i in range(1,101,1):
        g.make_step()

        if verbose and i % 10 == 0:
            print(f'step {i}:')
            print(g.str_zeros())
    print(f'part1 answer: {g.num_flashes}')

    g2 = octopus_graph(data)
    for i in range(1,301,1):
        if g2.make_step():
            print(f'Octupuses synced on step {i}!')
            break


if __name__ == "__main__":
    solution(verbose=False)