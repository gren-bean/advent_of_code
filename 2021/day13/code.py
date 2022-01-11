"""
Advent of Code 2021 Problem 13

Part1: Find number of marks after first fold
Part2: Complete all folds and view resulting message!
"""

def read_input(filename, verbose=False):
    """Read and Process Input"""    
    
    data = []
    with open(filename,"r") as f:
        lines = f.readlines()
    
    # Process input
    for line in lines:
        data.append(line.strip())
    return data


class paper_grid():
    """Represents a 2-D grid of paper"""

    def __init__(self, data, width=11, height=15, verbose=False):
        """
        Initialize paper grid

        :param data: list of mark positions followed by folds
        :param width: (int) grid width
        :param height: (int) grid height
        :param verbose: (bool) verbosity/debugging
        """
        self.verbose = verbose
        self.w = width
        self.h = height
        self.folds = []
        self.fold_ups = []
        self.fold_lefts = []
        self.grid = [['.' for i in range(self.w)] for i in range(self.h)]
        for d in data:
            if d[:2] == 'fo':
                fold = d.split('=')
                self.folds.append(fold[0][-1:])
                if fold[0][-1:] == 'y': self.fold_ups.append(int(fold[1]))
                if fold[0][-1:] == 'x': self.fold_lefts.append(int(fold[1]))
            elif len(d) > 0:
                pos = d.split(',')
                self.grid[int(pos[1])][int(pos[0])] = '#'


    def __str__(self):
        """Return string representation of grid"""
        return '\n'.join([''.join(row) for row in self.grid])


    def fold_up(self):
        """
        Splits grid in half and folds bottom portion of the paper up
        """

        # fold bottom half up
        dist = self.fold_ups.pop(0)
        # dist = self.h - 1 / 2
        for y in range(dist):
            for x in range(self.w):
                if self.grid[y][x] == '#' or self.grid[self.h - 1 - y][x] == '#':
                    self.grid[y][x] = '#'

        # Chop off bottom half and update height
        self.grid = [self.grid[row] for row in range(dist)]
        self.h = len(self.grid)


    def fold_left(self):
        """
        Splits grid in half and folds right over left
        """

        # fold bottom half up
        dist = self.fold_lefts.pop(0)
        # dist = self.h - 1 / 2
        for x in range(dist):
            for y in range(self.h):
                if self.grid[y][x] == '#' or self.grid[y][self.w - 1 - x] == '#':
                    self.grid[y][x] = '#'

        # Chop off right half
        self.grid = [[self.grid[row][x] for x in range(dist)] for row in range(self.h)]
        self.w = len(self.grid[0])


    def fold(self):
        """Single fold"""
        fold_type = self.folds.pop(0)
        if fold_type == 'x': self.fold_left()
        else: self.fold_up()


    def fold_up_paper(self):
        """Fold up the paper the whole (rest) of the way"""
        num_folds = len(self.folds)
        for i in range(num_folds):
            fold_type = self.folds.pop(0)
            if fold_type == 'x': self.fold_left()
            else: self.fold_up()


    def count_marks(self):
        """Counts marks"""
        num_marks = 0
        for row in range(self.h):
            for col in range(self.w):
                if self.grid[row][col] == '#': num_marks += 1
        return num_marks


def solution(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    pg = paper_grid(data, width=1311, height=895)
    # pg = paper_grid(data)
    # print(pg)
    # print('='*40)
    pg.fold()
    # print(pg)
    # print('='*40)
    # pg.fold_left()
    # print(pg)
    print(f'part1 answer {pg.count_marks()}')
    pg.fold_up_paper()
    print(f'part2 answer can be read in the below...')
    print(pg)


if __name__ == "__main__":
    solution(verbose=False)