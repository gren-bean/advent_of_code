"""
Advent of Code Problem 11

See Readme for details

"""

class solver():
    # Uses a grid to solve.
    # "Adjacent" = horizontal, vertical, or diagonal
    char_map = {"L":0,"#":1,".":-1}
    char_map_rev = {0:"L",1:"#",-1:"."}

    def __init__(self, data, part, verbose=0):
        self.verbose = verbose
        self.part = part
        self.grid = []
        self.last_row = len(data)-1
        self.last_col = len(data[0])-1
        
        # Builds the grid
        # Convert to numbers for easier computation
        # Assumes every row is same size
        for d in data:  # Loop through lines
            row = []
            for c in d: # Loop through characters    
                row.append(self.char_map[c])
            self.grid.append(row)


    def print_grid(self):
        """Prints grid in current state"""
        print("=" * 80)
        for l in self.grid:
            line = ""
            for num in l:
                line += self.char_map_rev[num]
            print(line)


    def update_cell(self, row, col):
        """
        Updates cell using simple set of rules

        :param i: row cell is in
        :param j: column cell is in
        :returns next_state: [0 or 1] cell's next state
        """

        if self.part == 1:
            # Get count of adjacent cells that are occupied (1)
            adjacent_count = 0
            for i in [-1,0,1]:
                curr_row = row + i
                if curr_row < 0 or curr_row > self.last_row:
                    continue    
                for j in [-1,0,1]:
                    curr_col = col + j
                    if curr_col < 0 or curr_col > self.last_col:
                        continue
                    # Make sure to skip over current cell
                    if i == 0 and j == 0: continue
                    if self.grid[curr_row][curr_col] == -1: continue
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
            

        # Part 2 solutions
        elif self.part == 2:

            # Get count of cells in view that are occupied (1)
            in_view = 0
            
            # Incrementor
            # - Each item represents increments to move [i,j]
            #   until an occupied seat is found
            incrementer = [[1,0], # looking down (south)
                        [-1,0],   # looking up (north)
                        [0,1],    # looking east
                        [0,-1],   # looking west
                        [1,1],    # looking southeast
                        [1,-1],   # looking southwest
                        [-1,-1],  # looking northwest
                        [-1,1]]   # looking northeast
            # Loop through different line of sights (8 total)
            for i in incrementer:
                seat_found = 0
                curr_row = row
                curr_col = col
                while seat_found == 0:
                    curr_row += i[0]
                    curr_col += i[1]

                    # Check we are still on grid
                    if curr_row < 0 or curr_row > self.last_row:
                        seat_found = 1
                    elif curr_col < 0 or curr_col > self.last_col:
                        seat_found = 1

                    # Check if first visited seat is occupied
                    elif self.grid[curr_row][curr_col] >= 0:
                        in_view += self.grid[curr_row][curr_col]
                        seat_found = 1

                # Debugging output
                if self.verbose >=2:
                    print(f"Seat [{row}][{col}]:")
                    print(f"\titerator: {i}")
                    print(f"\tstopped at position: [{curr_row}][{curr_col}]")
                    print(f"\toccupied seats in view: {in_view}")

            # Debugging output
            # if self.verbose >=2:
            #     print(f"Seat [{row}][{col}] | occupied seats: {in_view}")

            # If a cell is empty (0) and there are no occupied cells
            # Within line of sight the cell becomes occupied (1).
            if self.grid[row][col] == 0 and in_view == 0:
                return 1

            # If a seat is occupied (1) and >= 5 adjacent cells are
            # within the line of sight, cell becomes empty (0)
            elif self.grid[row][col] == 1 and in_view >= 5: 
                return 0
        
        else:
            print("ERROR: Unexpected parameter for 'part' of solver.")

        # Otherwise, cell doesn't change
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
            # Print current grid
            if self.verbose >= 1:
                self.print_grid()

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
    s = solver(data, 1, verbose=verbose)
    s.run_simulation()
    

def part2(verbose=0):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)      
    s = solver(data, 2, verbose=verbose)
    s.run_simulation()

def main(verbose=0):
    # part1(verbose=verbose)
    part2(verbose=verbose)

if __name__ == "__main__":
    main(verbose=0)