"""
Advent of Code 2021 Problem 12

Part1: Find every simple path through the caves, allowing multiple visits to big caves
Part2: Same as part1, but each path can have up to 1 small cave visited twice
"""

def read_input(filename, verbose=False):
    """
    Read and Process Input
    """ 
    data = []
    with open(filename,"r") as f:
        lines = f.readlines()

    # Process input
    for line in lines:
        data.append(line.strip())
    return data


class cave_graph():

    def __init__(self, data, verbose=False):
        """
        Set up object representation of cave

        :param data: list of connected nodes
        """
        self.verbose = verbose # Controls verbosity/debugging
        self.c_graph = {}  # Graph of cave
        self.path = []     # Tracks path during search of graph
        self.num_paths = 0 # Number of paths discovered
        self.vtf = True       # Visited twice flag, for part2 of problem
        # Build Graph, input only contains unique node-pairs
        for d in data:
            nodes = d.split('-')
            # Update graph with both nodes
            if nodes[0] not in self.c_graph:
                self.c_graph[nodes[0]] = {
                    'v':0,  # visited or not
                    'nbrs': [nodes[1]],  # neighbor nodes
                    'big_cave': nodes[0].isupper()  # If it's a big cave or not
                }
            else:
                 self.c_graph[nodes[0]]['nbrs'].append(nodes[1])
            if nodes[1] not in self.c_graph:
                self.c_graph[nodes[1]] = {
                    'v':0,  # visited or not
                    'nbrs': [nodes[0]],  # neighbor nodes
                    'big_cave': nodes[1].isupper()  # If it's a big cave or not
                }
            else:
                 self.c_graph[nodes[1]]['nbrs'].append(nodes[0])

    def __str__(self):
        output = ''
        for u in self.c_graph:
            output += (f"{u} -\n\tNeighbors: {self.c_graph[u]['nbrs']}"
                f"\n\tVisited: {self.c_graph[u]['v']}\n")
        return output


    def dfs_explore(self, v):
        """
        Recursive DFS exploration of graph
        
        :param v: (string) starting node
        :returns: True/False on if path was found
        """

        # Check if path was found
        if v == 'end':
            self.num_paths += 1
            if self.verbose: print(f"{','.join(self.path)},end")
            return True

        # Otherwise, continue exploring until dead end
        self.path.append(v)  # Update path
        # Mark node visited if it is NOT a big cave
        if not self.c_graph[v]['big_cave']:
            self.c_graph[v]['v'] += 1

        path_found = False
        for u in self.c_graph[v]['nbrs']:
            # If not yet visited, explore node
            if self.c_graph[u]['v'] == 0:
                if self.dfs_explore(u): path_found = True
            
            # [Part2] if (small cave) has been visited, but we have
            # Not yet visited a small cave twice, we can still
            # Explore it
            elif self.c_graph[u]['v'] == 1 and not self.vtf:
                self.vtf = True  # Flag that a small cave was visited twice
                if self.dfs_explore(u): path_found = True
        
        # Back-tracking component - mark node unvisited before returning
        if self.c_graph[v]['v'] == 2: self.vtf = False  # reset flag
        if self.c_graph[v]['v'] > 0: self.c_graph[v]['v'] -= 1 
        self.path.pop()
        return path_found


    def find_all_paths(self):
        """Finds all paths from start -> end given certain constraints"""
        
        # Reset graph
        self.num_paths = 0
        self.path = []
        self.c_graph['start']['v'] = 1
        
        # Explore all paths
        self.dfs_explore('start')
        return self.num_paths


def solution(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    
    c = cave_graph(data, verbose=verbose)
    print(f'part1 answer: {c.find_all_paths()}')
    c.vtf = False
    print(f'part2 answer: {c.find_all_paths()}')


if __name__ == "__main__":
    solution(verbose=False)