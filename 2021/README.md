# Advent of Code 2021
Advent of Code 2021 Solutions!
Author: Ben Greene

## Welcome
These are my notes on solving Advent of Code 2021. The challenges were not completed competitively for time.

## Notes on Each Day

### Day 1
- Part1:
	- Simple loop that compares to previous
- Part2:
	- Expansion of part1, need to calculate simple moving averages first.

### Day 2
- No significant notes, straightforward [x,y,direction] tracking.

### Day 3
- Converted input into a 2-D list, and then processed by columns
- Part2 was a bit trickier. It's a type of search, I believe with complexity `nm` in the worst case since you need to go down each column.

### Day 4
- Day 4 lends itself to defining a few objects to represent the bingo board and subsequent checks we may want to do on a bingo board.

### Day 5
- Simple 2-D coordinate math

### Day 6
- Part 1 is simple list modification that can be brute-forced if every fish is a number and we maintain a list of fishes. *Note: Updated with a better solution described in Part2 notes*
- Part 2 is the first challenge where we need to do an additional level of abstraction. The fish can be broken down into 6 different "generations" represented by a number, with new-born fish handled as an edge case for 2 cycles. From there, we rotate through the generations, updating the # of fish in each.