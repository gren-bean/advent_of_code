"""
Advent of Code Problem 11

See Readme for details

"""

class solver():
    # Uses a grid to solve.
    # "Adjacent" = horizontal, vertical, or diagonal

    def __init__(self, data, verbose=0):
        self.verbose = verbose
        self.grid = []
        self.last_row = len(data)-1
        self.last_col = len(data[0])-1

        # Builds the grid
        # Convert to numbers for easier computation
        # Assumes every row is same size
        for d in data:  # Loop through lines
            row = []
            for c in d: # Loop through characters
                # Empty
                if c == "L":
                    row.append(0)
                # Occupied
                elif c == "#":
                    row.append(1)
                # Ground - static
                elif c == ".":
                    row.append(-1)
                else:
                    print("ERROR: Unexpected input character")
            self.grid.append(row)


    def update_cell(self, row, col):
        """
        Updates cell using simple set of rules

        :param i: row cell is in
        :param j: column cell is in
        :returns next_state: [0 or 1] cell's next state
        """

        # Get count of adjacent cells that are occupied (1)
        adjacent_count = 0
        for i in [-1,0,1]:
            curr_row = row + i
            if 0 <= (row + i) <= self.last_row:
                for j in [-1,0,1]:
                    if 0 <= (col + j) <= self.last_col:
                        # Make sure to skip over current cell
                        if i == 0 and j == 0: continue
                        if self.grid[row+i][col+j] == -1: continue
                        # print(f"row: {row} | col: {col} | i:{ i} | j: {j}")
                        # Check if this adjacent cell is alive
                        adjacent_count += self.grid[row+i][col+j]

        # If a cell is empty (0) and there are no occupied cells adjacent, 
        # the cell becomes occupied (1).
        if self.grid[row][col] == 0 and adjacent_count == 0:
            return 1

        # If a seat is occupied (1) and >= 4 adjacent cells are occupied,
        # cell becomes empty (0)
        elif self.grid[row][col] == 1 and adjacent_count >= 4: 
            return 0
        
        # Otherwise, cell doesn't change
        else:
            return self.grid[row][col]

    def update_grid(self):
        """Updates grid using simple set of rules"""
        new_grid = []

        # Loop over rows and columns
        for i in range(len(self.grid)):
            new_row = []
            for j in range(len(self.grid[i])):
                # Check for static unit
                if self.grid[i][j] < 0:
                    new_row.append(-1)
                # Otherwise get new cell value
                else:       
                    new_row.append(self.update_cell(i, j))
            new_grid.append(new_row)
        return new_grid


    def run_simulation(self):
        """
        Runs seat simulation until steady-state
        
        :returns occupied_seats: (int) # occupied seats
        """
        occupied_seats = 0
        run = 1
        run_count = 0
        # Loop until steady-state
        while run == 1:
            new_grid = self.update_grid()
            run_count += 1
            if new_grid == self.grid:
                self.grid = new_grid.copy()
                run = 0
                continue
            else:
                self.grid = new_grid.copy()
        
        # Calculate occupied seats:
        for row in self.grid:
            for seat in row:
                if seat == 1:
                    occupied_seats += 1

        print(f"steady-state reached in {run_count} runs")
        print(f"occupied seats: {occupied_seats}")


def read_input(filename, verbose=0):
    """
    Read in Input

    Requires:
    - file to be in current working directory
    """
    data = []
    with open(filename,"r") as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.strip())
    return data


def part1(verbose=0):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    s = solver(data, verbose=verbose)
    s.run_simulation()
    

def part2(verbose=0):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)      

def main(verbose=0):
    part1(verbose=verbose)
    # part2(verbose=verbose)

if __name__ == "__main__":
    main(verbose=0)