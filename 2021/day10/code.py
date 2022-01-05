"""
Advent of Code 2021 Problem 10

Part1: Find lines with syntax errors, ignore incomplete lines
Part2: Determine what is needed to finish incomplete lines
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


def solution(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    
    # Scoring
    p1_scores = {')':3, ']':57, '}':1197, '>':25137}
    p2_scores = {')':1, ']':2, '}':3, '>':4}
    p1_final_score = 0
    p2_final_score = []

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
        valid_line = True
        for c in line:
            # Opening bracket character
            if c in ob:
                expected.append(ob[c])

            # Closing bracket character
            elif c in cb:
                # Pop expected closing character using FIFO
                e = expected.pop()
                if c != e:
                    if verbose: print(f"Syntax Error on line {line_num}, char '{c}' when '{e}' was expected.")
                    p1_final_score += p1_scores[c]
                    valid_line = False
                    break

            # Non-bracket character - skip it
            else: continue

        # -------- PART 2 logic ----------
        # Line is valid but incomplete incomplete
        if valid_line:
            s = 0
            # Iterate back through FIFO queue
            for i in reversed(range(len(expected))):
                s = s*5 + p2_scores[expected[i]]
            p2_final_score.append(s)

        line_num += 1  # increment line number

    p2_final_score = sorted(p2_final_score)[int(len(p2_final_score)/2)]
    print(f'part1 answer: {p1_final_score}')
    print(f'part2 answer: {p2_final_score}')


def part2(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    # Do stuff
    pass


if __name__ == "__main__":
    solution(verbose=False)