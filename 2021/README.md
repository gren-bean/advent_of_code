# Advent of Code 2021
Advent of Code 2021 Solutions!
Author: Ben Greene

## Welcome
These are my notes on solving Advent of Code 2021. The challenges were only completed for fun.

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
- **Part 1** is simple list modification that can be brute-forced if every fish is a number and we maintain a list of fishes. *Note: Updated with a better solution described in Part2 notes*
- **Part 2** is the first challenge where we need to do an additional level of abstraction. The fish can be broken down into 6 different "generations" represented by a number, with new-born fish handled as an edge case for 2 cycles. From there, we rotate through the generations, updating the # of fish in each.

### Day 7
- **Part1**: We are looking for the point (number) with shortest distance from all points in our input. Research brought us to the **geometric median**. The 1-D case of this is simply the **median**, which we can find in `O (n log n)` in the lazy case.
- **Part2**: The problem is updated so that Fuel Consumption becomes an *arithmetic progression* (versus constant) where each value is +1 from the previous, with an example of how this works below:
    ```
    steps moved   | 01 02 03 04 05 06 07 08 09 10 11
    fuel per step | 01 02 03 04 05 06 07 08 09 10 11
    total fuel    | 01 03 06 10 15 21 28 36 45 55 66
    ```
    - The "Total Fuel" cost is a type of "Triangle Numbers" sequence. The equation for the `nth` number is `n(n+1)/2` or `n^2/2 + n/2` (from Wikipedia, and there is a clever way to visualize this with rectangles)
    - In our equation, `n^2` will dominate, *so the goal is to minimize the `n^2` for all the movements*, which is equivalent to finding the **mean**
    - Intuitively, this makes sense for our solution - the more steps that will be needed, the heavier the Fuel Conumption will be weighted. The **mean** will effectively represent this for us.
    - Finally, we will search a few positions around the mean (+/- 5) to account for some rounding errors and potential weirdness in the data,

- Useful references
    1. https://en.wikipedia.org/wiki/Central_tendency
    2. https://en.wikipedia.org/wiki/Median
    3. https://en.wikipedia.org/wiki/Geometric_median
    4. https://rcoh.me/posts/linear-time-median-finding/ - If we wanted to find median in linear time, but this was not implemented.
    5. https://en.wikipedia.org/wiki/Arithmetic_progression
    6. https://en.wikipedia.org/wiki/Triangular_number
    7. https://www.johnmyleswhite.com/notebook/2013/03/22/modes-medians-and-means-an-unifying-perspective/ - This is an excellent reference on representing a dataset's *Central Tendency*

### Day 8
- **Part1**: Simple warm up, really just meant to get you familiar with data format.
- **Part2**: Required analyzing the specifics of the problem to come up with how to map each combination for digits that could not be uniquely identified by their signal length. The core strategy was:
    1. Define the unique "position signatures" for the number signals of lengths 5 and 6 (which corresponded to `2|3|5|6|9`) .
    2. Use the easily spotted digits of `1`, `4`, and `7` to narrow the decoding search space (for character position mappings) down to 8 possible mappings per signal (from an original of 5040 combinations). Given the small input, a more brute force approach could have skipped this first step, but narrowing the search space is more efficient by a factor of x100 or more.
    3. For each signal, iterate through the 8 possible decodings to find the unique solution.
    4. Apply that solution to decode the output.
- *Note: logic for part 2 is a bit messy! Tried to take advantage of python sets, but sorted lists were also a benefit*

### Day 9
- **Part1**: Representing the 2-D grid as an adjaceny list graph made searching for the low points much easier. The lowest points are simply the points where all neighboring nodes are higher value.
- **Part2**: Starting from each of the lowest points in Part1, we can run a breadth-first search out to the ridgelines (defined as nodes of height `9`) to determine basin sizes

### Day 10
- Both parts of this challenge were solved maintaining a FIFO queue of expected closing bracket characters for each line, using a python `list` 

### Day 11
- Maintain the 10 x 10 grid of "octopuses" as nodes in a connected graph (similar to day 9)
- For each step, all octopuses increase energy level by 1. From there, used an adaption of BFS to enact impact on neighboring nodes

### Day 12
- **Part1**: First explicit graph problem! Objective is to find every simple path in the graph, with the caveat that "big caves" can be visited more than once in a path. We can do this with **Depth-First Search (DFS)** implemented with **Back-Tracking**.
- **Part2**: Additional complexity is added by allowing **one** small cave to be visited **twice** within each path. This is solved by updating the node 'visited' attribute to an integer in order to track number of visits, and a flag variable `vtf` to track whether a small cave has been visited twice or not along the current path.

### Day 13
- **Part1**: Simulated paper folding. The paper can be simulated by a 2-D matrix. And then folding is equivalent to cutting at the fold line, and slide. *Importantly, all of the folds involve folding the paper in half, which simplifies this problem significantly when compared to the case where non-equal folds are allowed.