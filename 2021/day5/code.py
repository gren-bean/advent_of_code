"""
Advent of Code 2021 Problem 5

Part1: Find the number of points where at least two lines overlap
Part2: Same as part1, but including diagonal lines
"""


class grid_map():
    """Object to represent a 2-D grid map that is N x N in size"""
    
    def __init__(self, size=1000, diagonals_on=False,verbose=False):
        """Build N x N grid"""
        self.N = size
        self.grid = [[0 for j in range(self.N)] for i in range(self.N)]
        self.verbose = verbose
        self.diagonals_on = diagonals_on

        # Stepper object for diagonal line updates to grid
        self.stepper = {'NW':(-1,-1), 'SW':(-1,1), 'NE':(1,-1), 'SE':(1,1)}


    def __str__(self):
        """Returns string representation to print"""
        output = ""
        for i in range(self.N):
            output = output + ' '.join([str(j) for j in self.grid[i]]) + '\n'
        return output


    def find_direction(self, line_seg):
        """
        Finds direction of a Diagonal line segment at 45 degree angle

        :param line_seg: (tuple of tuples) (X,Y) endpoints of line segment
        :returns direction: (str) one of 'NE','SE','SW','NW', or 'unknown'
        """
        if line_seg[0][0] > line_seg[1][0] and line_seg[0][1] > line_seg[1][1]:
            return 'NW'
        elif line_seg[0][0] > line_seg[1][0] and line_seg[0][1] < line_seg[1][1]:
            return 'SW'
        elif line_seg[0][0] < line_seg[1][0] and line_seg[0][1] > line_seg[1][1]:
            return 'NE'
        elif line_seg[0][0] < line_seg[1][0] and line_seg[0][1] < line_seg[1][1]:
            return 'SE'
        else:
            return 'unknown'

    def update(self, line_seg):
        """
        Updates grid with vertical or horizontal line

        :param line_seg: (tuple of tuples) (X,Y) endpoints of line segment
        """

        # Vertical line - X's are the same
        if line_seg[0][0] == line_seg[1][0]:
            start = min((line_seg[0][1], line_seg[1][1]))
            end = max((line_seg[0][1], line_seg[1][1])) + 1
            # Move along grid vertically, with endpoints inclusive
            for i in range(start, end, 1):
                self.grid[i][line_seg[0][0]] += 1

        # Horizontal line - Y's are the same
        elif line_seg[0][1] == line_seg[1][1]:
            start = min((line_seg[0][0], line_seg[1][0]))
            end = max((line_seg[0][0], line_seg[1][0])) + 1
            # Move along grid horizontally, with endpoints inclusive
            for i in range(start, end, 1):
                self.grid[line_seg[0][1]][i] += 1

        # Diagonal lines - Line that is NOT horizontal or vertical
        # Problem description specifies ONLY 45-degree lines
        elif not self.diagonals_on:
            if self.verbose: print('WARNING: Line detected that is not horizontal or vertical')
        else:
            _dir = self.find_direction(line_seg)
            _x = line_seg[0][0]
            _y = line_seg[0][1]
            self.grid[_y][_x] += 1
            while _x != line_seg[1][0] or _y != line_seg[1][1]:
                _x += self.stepper[_dir][0]
                _y += self.stepper[_dir][1]
                self.grid[_y][_x] += 1


    def count_crosses(self, cutoff=2):
        """
        Counts places where at least 2 lines cross

        :param cutoff: (int) minimum number of crosses
        :returns cnt: (int) number of spots with crosses above cutoff
        """
        cnt = 0
        for i in range(self.N):
            for j in range(self.N):
                if self.grid[i][j] >= cutoff: cnt += 1
        return cnt


def read_input(filename, verbose=False):
    """
    Read in Input and do some basic parsing based on problem specifics
    Requires:
    - file to be in current working directory
   """ 

    # Read file
    with open(filename,"r") as f:
        lines = f.readlines()

    # Parse data
    data = []  # List of tuples of tuples
    for line in lines:
        coords = line.split(' -> ')
        if len(coords) < 2: continue

        # Parse starting position
        temp = coords[0].split(',')
        start = (int(temp[0]),int(temp[1]))
    
        # Parse stopping position
        temp = coords[1].split(',')
        stop = (int(temp[0]),int(temp[1]))

        data.append((start,stop))

    return data


def part1(verbose=False):
    input_file = "input.txt"
    
    # Data is a list of tuples of coordinates like:
    #   [ ( (start_x, start_y), (stop_x, stop_y) ), ... ]
    data = read_input(input_file, verbose=verbose)
    g = grid_map()
    for d in data:
        g.update(d)

    print(f'answer part1: {g.count_crosses()}')



def part2(verbose=False):
    input_file = "input.txt"
    # Data is a list of tuples of coordinates like:
    #   [ ( (start_x, start_y), (stop_x, stop_y) ), ... ]

    data = read_input(input_file, verbose=verbose)
    g = grid_map(diagonals_on=True)
    for d in data:
        g.update(d)
    print(f'answer part2: {g.count_crosses()}')


if __name__ == "__main__":
    try:
        part1(verbose=False)
        part2(verbose=False)
    except Exception as err:
        print(f'ERROR: {err}')