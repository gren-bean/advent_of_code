"""
Advent of Code 2021 Problem 8

Part1: Find number of unique sequences corresponding to digits 1, 4, 7 and 8
Part2: Use signal patterns to decode full output

Numbers are displayed as such:
      0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

      5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg
"""

def read_input(filename, verbose=False):
    """
    Read in Input

    Requires:
    - file to be in current working directory
    """ 
    data = {}
    with open(filename,"r") as f:
        lines = f.readlines()

    # Process input
    _id = 0
    for line in lines:
        segments = line.split('|')
        if len(segments) < 2: continue
        data[_id] = {
            'signal':segments[0].strip().split(),
            'output':segments[1].strip().split()
        }
        _id += 1
    return data


def part1(verbose=False):
    input_file = "input.txt"

    # Data is a dictionary, with each entry containing
    # the 10 unique signal patterns and 4-digit output value
    data = read_input(input_file, verbose=verbose)
    
    # Unique signal lengths
    usl = [2, 3, 4, 7]
    total_cnt = 0
    for d in data:
        cnt = [1 for o in data[d]['output'] if len(o) in usl]
        total_cnt += sum(cnt)
    print(f'part1 answer: {total_cnt}')


def part2(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)

    """
    Defined positions via a number (defined as string) like so:
         0000
        1    2
        1    2
         3333
        4    5
        4    5
         6666
    """

    """
    pos_mappings - holds possible mappings for positions 0 - 6.
      - Signals for 1, 4, 7, and 8 are KNOWN
      - There are always 8 possible mappings given the KNOWN signals
      - Opposities will be: 1|3, 2|5, 4|6
      - Position 0 is always known
    """
    pos_mappings = [
        [0, 0, 0, 1, 0, 1, 1],
        [0, 0, 1, 1, 0, 0, 1],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 1],
        [0, 1, 1, 0, 0, 0, 1],
        [0, 1, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0]
    ]
    
    """
    Each signal will have a unique signature
        - signal_chars_easy: uses length of signal string to decode 1|4|7|8
        - signal_chars_hard: uses signature of positions to decode 0|2|3|5|6|9
    """
    # Dict for char count -> Number
    signal_chars_easy = {
        2:'1',
        3:'7',
        4:'4',
        7:'8'
    }
    # Dict for signal chars -> Number
    signal_chars_hard = {
        '0': set('012456'),  # 0
        '2': set('02346'),   # 2
        '3': set('02356'),   # 3
        '5': set('01356'),   # 5
        '6': set('013456'),  # 6
        '9': set('012356')   # 9
    }

    # Decode each row based on signal wires
    outputs = []
    for d in data:

        if verbose:
            print('-'*50)
            print(f"Signal - {data[d]['signal']}")
            print(f"Output - {data[d]['output']}")

        chars = ['a','b','c','d','e','f','g']
        
        # Decode Map 1: Positions => Possible Chars
        d_map1 = {
            '0':[],
            '1':[],
            '2':[],
            '3':[],
            '4':[],
            '5':[],
            '6':[]
        }
        # Decode Map 2: Char => Position (gets filled out later)
        d_map2 = {}

        # Extract known signals for 1, 4, 7
        # Use to define possible mappings
        for _s in data[d]['signal']:
            if len(_s) == 2:
                one_signal = _s
            elif len(_s) == 3:
                seven_signal = _s
            elif len(_s) == 4:
                four_signal = _s

        # Set possible values based on known signals
        d_map1 ['2'] = sorted(one_signal)
        d_map1 ['5'] = sorted(one_signal)
        for _c in seven_signal:
            if _c not in one_signal:
                d_map1 ['0'] = sorted(_c)
                chars.remove(_c) 
                break
        for _c in four_signal:
            chars.remove(_c) 
            if _c not in one_signal:
                d_map1 ['1'].append(_c) 
                d_map1 ['3'].append(_c)
        for _c in chars:
            d_map1 ['4'].append(_c) 
            d_map1 ['6'].append(_c) 

        # Try possible decoding maps until we find correct one
        valid_map = False # Set flag
        for _m in pos_mappings:
            d_map2 = {
                d_map1['0'][_m[0]]: '0',
                d_map1['1'][_m[1]]: '1',
                d_map1['2'][_m[2]]: '2',
                d_map1['3'][_m[3]]: '3',
                d_map1['4'][_m[4]]: '4',
                d_map1['5'][_m[5]]: '5',
                d_map1['6'][_m[6]]: '6'
            }

            # Loop through signal values to test decoding
            matches = 0
            for _s in data[d]['signal']:
                if len(_s) == 5 or len(_s) == 6:
                    sequence = ''
                    # Build signature
                    for _c in _s:
                        sequence += d_map2[_c]
                    
                    # Check signature is valid
                    # If signature is NOT valid, we have a faulty mapping
                    if set(sequence) in signal_chars_hard.values():
                        matches += 1
                    else:
                        break  # Invalid sequence, try new map

                # If we have matched all unique 5/6 length signals, we have a valid map
                if matches == 6:
                    valid_map = True
                    break

            if valid_map == True:
                break

        if valid_map == False:
            print(f"ERROR! No valid map found for signal - {data[d]['signal']}")
            return

        # Use d_map2 to decode numbers
        _o = ''
        for _s in data[d]['output']:
            if len(_s) in signal_chars_easy: _o += signal_chars_easy[len(_s)] 
            else:
                sequence = ''
                for _c in _s:
                    sequence += d_map2[_c]
                for _k in signal_chars_hard:
                    if set(sequence) == signal_chars_hard[_k]:
                        _o += _k
                        break
        if verbose:
            print(f'Mapping Discovered - {d_map2}')
            print(f'Decoded output - {_o}')
        outputs.append(_o)

    # Calculate solution
    s = 0
    for _o in outputs:
        s += int(_o)
    print(f'part2 answer: {s}')


if __name__ == "__main__":
    part1(verbose=False)
    part2(verbose=False)