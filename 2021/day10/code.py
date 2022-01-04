"""
Advent of Code 2021 Problem 10

Part1: TBD
Part2: TBD
"""

def read_input(filename, verbose=False):
    """
    Read in Input
    """ 
    data = []
    with open(filename,"r") as f:
        lines = f.readlines()
    
    # Process input
    for line in lines:
        data.append(line.strip())
    return data


def part1(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    
    # Open Brackets paired w/ expected closing
    ob = {
        '(':')',
        '[':']',
        '{':'}',
        '<':'>'
    }
    cb = (')', ']', '}', '>') # Closing Brackets
    syntax_errors = [] # List of chars that caused syntax error

    # Find corrupted lines
    # NOTE - some lines can be incomplete (closing brackets not observed)
    line_num = 0
    for line in data:
        expected = [] # List of expected closing brackets maintained as FIFO
        syntax_error = ''  # Character we found instead of expected char
        try:
            for c in line:
                # Opening bracket character
                if c in ob:
                    expected.append(ob[c])

                # Closing bracket character
                elif c in cb:
                    # Pop expected closing character using FIFO
                    e = expected.pop()
                    if c != e:
                        syntax_error = c
                        raise SyntaxError

                # Non-bracket character - skip it
                else: continue


            # Check that all closing brackets have been observed
            # if len(expected) > 0:
            #     e = expected.pop()
            #     raise SyntaxError

        # Catch syntax errors
        except SyntaxError:
            if verbose: print(f"Syntax Error on line {line_num}, error with char '{e}'")
            syntax_errors.append(syntax_error)

        line_num += 1  # increment line number

    # Calculate score
    scores = { ')':3, ']':57, '}':1197, '>':25137}
    final_score = sum([scores[se] for se in syntax_errors])
    print(f'part1 answer: {final_score}')


def part2(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    # Do stuff
    pass


if __name__ == "__main__":
    part1(verbose=False)
    part2(verbose=False)