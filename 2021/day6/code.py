"""
Advent of Code 2021 Problem 6

Part1: Propagate lantern fish for 80 days
Part2: Propagate lantern fish for 256 days
"""

def read_input(filename, verbose=False):
    """Read in Input """
    with open(filename,"r") as f:
        lines = f.readlines()
    # Process input
    data = [int(i) for i in lines[0].split(',')]
    return data


def part1(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    # Time variables
    days = 80
    r_cycle = 7  # reproduction cycle in days

    # "Generations" list holds number of fish in in each "Generation"
    # Generations are uniquely identified by their index in the list
    gens = [0] * r_cycle
    newborn = 0  # Fish that were just born
    dayold = 0   # Fish that are 1 day old
    gen_ptr = 0  # Points to the current generation about to reproduce

    # Initial setup
    for f in data:
        gens[f] += 1

    for n in range(days):
        two_dayold = dayold         # Temp variable to hold 2-day-olds
        dayold = newborn            # Yesterday's newborns turn 1dayold
        newborn = gens[gen_ptr]     # Reproduce
        gens[gen_ptr] += two_dayold # Update generation for next cycle
        
        # Update generational pointer
        if gen_ptr == (r_cycle - 1): gen_ptr = 0
        else: gen_ptr += 1

    # Answer is sum of our all generations, plus newborns and 1-day-olds
    print(f'Total fishes after {days} days: {sum(gens) + newborn + dayold}')


    # BRUTE FORCE METHOD - This is Slow!!!
    # timer = r_cycle - 1
    # for n in range(days):
    #     new_fishes = 0
    #     # Run through alive fishes
    #     for i in range(len(data)):
    #         if data[i] == 0:
    #             new_fishes += 1
    #             data[i] = 6  # reset timer
    #         else: data[i] -= 1
    #     # Make new fishes
    #     for i in range(new_fishes):
    #         data.append(8)
    # print(f'Total fishes after {days} days: {len(data)}')


def part2(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    
    # Time variables
    days = 256
    r_cycle = 7  # reproduction cycle in days

    # "Generations" list holds number of fish in in each "Generation"
    # Generations are uniquely identified by their index in the list
    gens = [0] * r_cycle
    newborn = 0  # Fish that were just born
    dayold = 0   # Fish that are 1 day old
    gen_ptr = 0  # Points to the current generation about to reproduce

    # Initial setup
    for f in data:
        gens[f] += 1

    for n in range(days):
        two_dayold = dayold         # Temp variable to hold 2-day-olds
        dayold = newborn            # Yesterday's newborns turn 1dayold
        newborn = gens[gen_ptr]     # Reproduce
        gens[gen_ptr] += two_dayold # Update generation for next cycle
        
        # Update generational pointer
        if gen_ptr == (r_cycle - 1): gen_ptr = 0
        else: gen_ptr += 1

    # Answer is sum of our all generations, plus newborns and 1-day-olds
    print(f'Total fishes after {days} days: {sum(gens) + newborn + dayold}')


if __name__ == "__main__":
    part1(verbose=False)
    part2(verbose=False)