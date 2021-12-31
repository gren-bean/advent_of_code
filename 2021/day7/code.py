"""
Advent of Code 2021 Problem 7

Part1: Align to same number with least overall cost (cost is simply difference value)
Part2: Align to same number with lease overall cost (cost is increasing arithmetic progression)
"""

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
    return [int(i) for i in lines[0].split(',')]


def nlogn_median(l):
    """Finds median of list 'l' in nlogn time"""
    l = sorted(l)

    # If 'l' is odd, return median value
    if len(l) % 2 == 1:
        return l[len(l) // 2] # This is correct bc of zero indexing
    
    # If 'l' is even, calculate and return median value
    else:
        return 0.5 * (l[len(l) // 2 - 1] + l[len(l) // 2])


def part1(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    
    # Find Median as location lowest distance
    median = nlogn_median(data)
    cost = sum([abs(d - median) for d in data])
    print(f'part1 answer: {cost}')


def part2(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)

    # Find Mean as location with lowest distance
    best_pos = round(sum(data)/len(data))
    if verbose: print(f'mean: {best_pos}')
    lowest_cost = sum( [ (abs(d - best_pos)*(abs(d - best_pos)+1))//2 for d in data] )
    # Search around mean
    for m in range(best_pos - 5, best_pos + 5):
        cost = sum( [ (abs(d-m)*(abs(d-m)+1))//2 for d in data] )
        if cost < lowest_cost:
            lowest_cost = cost
            best_pos = m
            if verbose: print(f'Better position found @ {m} with cost {cost}')
    print(f'part2 answer: position @ {best_pos} with cost {lowest_cost}')


if __name__ == "__main__":
    part1(verbose=False)
    part2(verbose=True)