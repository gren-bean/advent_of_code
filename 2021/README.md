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
    4. https://rcoh.me/posts/linear-time-median-finding/ - If we wanted to find median in linear time
    5. https://en.wikipedia.org/wiki/Arithmetic_progression
    6. https://en.wikipedia.org/wiki/Triangular_number
    7. https://www.johnmyleswhite.com/notebook/2013/03/22/modes-medians-and-means-an-unifying-perspective/
        - Excellent reference on representing a dataset's *Central Tendency*

### Day 8
