"""
Advent of Code 2021 Problem 9

Part1: Find lowest areas on 2D grid map
Part2: Find sizes of 3 largest basins
"""

class grid_graph():
    """Represents 2-D grid map as a graph"""

    def __init__(self, data):
        """
        Initialize NxN Grid Map
        
        :param data: list of lists to represent 2-D matrix
        """
        # Simple error check
        if len(data) != len(data[0]):
            print('ERROR: Data has different number of rows and columns!')
            # return

        # Represent 2-D grid matrix as a graph
        uid = 0
        self.size = len(data) # Size of grid
        self.grid = {}  # Grid represented as graph adjacency list
        self.lowest_points = []  # Holds list lowest nodes
        for row in range(self.size):
            for col in range(self.size):
                # Build list of neighbors
                nbs = []

                # Neighbors in adjacent rows
                for r in [-1, 1]:
                    if 0 <= (row + r) < self.size:
                        nbs.append(uid + r*self.size)
                # Neighbors in adjacent columns
                for c in [-1, 1]:
                    if 0 <= (col + c) < self.size:
                        nbs.append(uid + c)

                # Add node to graph     
                self.grid[uid] = {
                    'ht': data[row][col], # Height
                    'visited': False,     # If it's been visited 
                    'nbrs': nbs           # Neighbors
                    }

                # Increment unique identifier
                uid += 1
        

    def __str__(self):
        """Return string representation"""
        output = ''
        for uid in self.grid:
            output = output + (f'Node: {uid}\n'
                f"\tweight: {self.grid[uid]['ht']}\n"
                f"\tvisited: {self.grid[uid]['visited']}\n"
                f"\tneighbors: {self.grid[uid]['nbrs']}\n")
        return output


    def find_valleys(self):
        """
        Finds valleys - i.e. low values with no lower values adjacent
        
        :return risk_score: (int) calculated based on requirements
        """
        risk_score = 0
        for u in self.grid:
            low_point = True
            
            # Scan neighbors for lower value
            for v in self.grid[u]['nbrs']:
                if self.grid[v]['ht'] <= self.grid[u]['ht']:
                    low_point = False
                    break

            # Calculate risk score
            if low_point:
                risk_score += self.grid[u]['ht'] + 1
                self.lowest_points.append(u)

        return risk_score


    def bfs(self, start):
        """
        Simple Breadth-first Search (BFS) to discover basin sizes
        
        :param u: (int) uid of starting node
        """
        basin_size = 0
        Q = [start]
        while len(Q) > 0:
            u = Q.pop(0)
            for v in self.grid[u]['nbrs']:
                # Check if node has already been visited
                if not self.grid[v]['visited']:
                    Q.append(v)
                    self.grid[v]['visited'] = True
                    basin_size += 1
        return basin_size


    def find_basins(self):
        """
        Finds Basins

        :return top3: (int) product of top 3 basin ints
        """

        # Populate lowest_points
        r = self.find_valleys()

        # Mark all ridges with height '9' as visited per
        # question parameters
        for u in self.grid:
            if self.grid[u]['ht'] == 9:
                self.grid[u]['visited'] = True

        # Breadth-first search starting from each of the low points
        basin_sizes = []
        for u in self.lowest_points:
            basin_sizes.append(self.bfs(u))        
        
        # Calculate product of top 3 basin sizes
        basin_sizes_sorted = sorted(basin_sizes)
        top3 = 1
        for b_size in basin_sizes_sorted[-3:]: top3 *= b_size
        return top3


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
        data.append([int(i) for i in line.strip()])
    return data


def part1(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    g = grid_graph(data)
    # print(g)
    print(f'part1 answer: {g.find_valleys()}')


def part2(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    g = grid_graph(data)
    print(f'part2 answer: {g.find_basins()}')

if __name__ == "__main__":
    part1(verbose=False)
    part2(verbose=False)