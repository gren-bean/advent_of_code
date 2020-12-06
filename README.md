# advent_of_code2020
Advent of Code 2020

Solved in Python!

## Todo:
- focus more on OO style for additional problems like the passport-parsing ones.

## Tips & Tricks to note:

- Debugging output is controlled by a `verbose` flag, set to `0/No debug` as a default. Values of `verbose=1` and `verbose=2` are accepted with the higher value increasing verbosity.
- **Day 1**:
  - Many clever possibilities, but the solutions in this repo are simple loops. Input was small so no need to do anything special.
- **Day 2**:
  - Got into some heavy use of dictionaries
- **Day 3**:
  - Simple indexing in a list, used the modulo `%` operator, but not much else.
- **Day 4**:
  - More dictionary use. 
  - Part2: used modular functions to make an easy to read and use program.
- **Day 5**: 
  - The hint was "binary partitioning". This problem is essentially converting a string into two binary numbers' base 10 equivalent. This is done via python's `int(str,base=2)`
  - Translating a string with python: ```python's str.translate(str.maketrans('old_chars','new_chars'))```, ref[1-2].
- **Day 6**:
  - For part1, we want unique characters out of each group. This is done via building a string and then collapsing it.
  - Unique characters in a list like `''.join(set('aaabcabccd'))`, ref[3].
  - For part2, we add the number of persons in each group as the only additional information we need. 
  - Ultimately unused, but interesting read is "best way to count char occurences in string" in ref[4]

## References
[1] https://stackoverflow.com/questions/41535571/how-to-explain-the-str-maketrans-function-in-python-3-6/41536036  
[2] https://discuss.python.org/t/str-replace-of-a-set-of-characters/2758/3  
[3] https://stackoverflow.com/questions/13902805/list-of-all-unique-characters-in-a-string  
[4] https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value  