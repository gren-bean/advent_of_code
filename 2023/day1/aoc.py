"""
Advent of code
Day 1
"""

import utils as utils

"""
Part1

On each line, the calibration value can be found by combining the first dig(it and the last digit (in that order) to form a single two-digit number.

"""
def p1():
    # data =  utils.read_input_strings('p1_test.txt')
    data = utils.read_input_strings('input.txt')
    sum = 0
    for l in data:
        sum += int(utils.str_first_digit(l) + utils.str_last_digit(l))
    print(sum)

# Part 2
def p2():
    # data = utils.read_input_strings('p2_test.txt')
    data = utils.read_input_strings('input.txt')
    sum = 0
    for l in data:
        _l = utils.convert_text_to_int(l)
        # print(f"{l} => {_l} => {utils.str_first_digit(_l) + utils.str_last_digit(_l)}")
        sum += int(utils.str_first_digit(_l) + utils.str_last_digit(_l))
    print(sum)

p1()
p2()