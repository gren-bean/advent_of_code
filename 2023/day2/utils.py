"""
Advent of Code Utilities file
Updated each day as more utilities were required
Day 2
"""

import re # regexes

def read_input_strings(filename):
    # Reads input and returns list of strings
    with open(filename, 'r') as input_file:
        d = [line.strip() for line in input_file]
    return d

def str_first_digit(s):
    # gets first digit in a string
    for c in s:
        if c.isdigit(): return c
    return None

def str_last_digit(s):
    # gets last digit in a string
    # first reverse string
    s = s[::-1]
    # then get first digit, which would be last
    for c in s:
        if c.isdigit(): return c
    return None

def convert_text_to_int(s):
    # Converts text in a string to digit counterpart (as a string)
    # Problem is words can overlap and you need to account for all numbers even in this case
    nums = {'one':'one1one', 'two':'two2two', 'three':'three3three', 'four':'four4four', 'five':'five5five', 'six':'six6six', 'seven':'seven7seven','eight':'eight8eight','nine':'nine9nine'}
    # can start at 3 since that's our smallest digit name
    for n in nums.keys():
        s = s.replace(n, nums[n])
    return s