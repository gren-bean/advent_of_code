"""
Advent of Code 2021 Problem 4

Part1: Find first winning bingo board based on sequence of numbers
Part2: Find last bingo board to win
"""

class bingo_board():
    """
    An object representing a bingo board with N x N spots

    The board is represented as a list of lists
    """

    def __init__(self, nums, N=5):
        """
        Create board

        :param nums: (list of str) sequential list of nums that read left -> right and top -> down. Must be of length N x X. 
        :param N: (int) board size
        """
        # Error Check        
        if len(nums) != (N * N):
            raise Exception(f'Bingo board passed {len(nums)} numbers to make an {N}x{N} board!')
        
        # Build Board
        self.board = []
        self.board_status = [[0 for i in range(N)] for i in range(N)]
        self.size = N
        for i in range(N):
            self.board.append(nums[i*self.size:(i+1)*self.size])


    def __str__(self):
        """Represents board as a printable string object"""
        output = ''
        for i in range(self.size):
            output = output + ' '.join(self.board[i]) + '\n'
        output = output + '='*self.size*2 + '\n'
        for i in range(self.size):
            output = output + ' '.join([str(num) for num in self.board_status[i]]) + '\n'
        
        return output


    def check_for_bingo(self):
        """Checks for bingo and returns True/False"""
        for i in range(self.size):
            # Check for Horizontal or Vertical Win
            if sum(self.board_status[i]) == self.size or \
            sum([self.board_status[j][i] for j in range(self.size)]) == self.size:
                return True


    def update(self,pick):
        """
        Checks board for number, and updates status. Then checks for a win

        :returns: True/False on bingo
        """
        # Update board
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] == pick:
                    self.board_status[row][col] = 1
                    if self.check_for_bingo():
                        return True
        return False


    def calc_final_score(self, pick):
        """Calculates answer per pre-defined rules

        :param pick: (int) integer value of last pick
        :returns final_score: (int) final score of board
        """

        # Sum of all unmarked numbers
        answer = 0
        for row in range(self.size):
            for col in range(self.size):
                if self.board_status[row][col] == 0:
                    answer += int(self.board[row][col])
        # Multiply sum by most recent pick
        answer *= pick
        return answer


def read_input(filename, verbose=False):
    """
    Read in Input

    Requires:
    - file to be in current working directory
   """ 

    # Read file
    with open(filename,"r") as f:
        lines = f.readlines()
    
    return lines


def create_boards(data, N=5):
    """
    Creates bingo boards

    :param N: (int) size of NxN bingo board
    """
    boards = {}  # Dictionary of bingo board objects
    temp_board = []  # Holds temporary bingo board
    unique_id = 1  # Unique numerical id of board 

    for line in data[1:]:
        if len(line.split()) > 2:
            for item in line.split():
                temp_board.append(item)
            # Check for a complete board
            if len(temp_board) >= (N*N):
                boards[unique_id] = {
                    'board':bingo_board(temp_board, N),
                    'win_order':-1
                }
                unique_id += 1  # Increment unique ID
                temp_board = [] # Clear temp board
        else:
            continue
    return boards


def part1(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)
    # Do stuff

    N = 5  # Size of bingo board
    chosen_nums = [] # Selected bingo numbers
    
    chosen_nums = data[0].split(',') 
    
    # Dict of bingo board objects
    boards = create_boards(data,N)

    for pick in chosen_nums:
        if verbose: print(f'Number {pick} chosen!')
        for b in boards:
            if boards[b]['board'].update(pick):
                print('BINGO!!! Winning Board:')
                print(boards[b]['board'])
                print(f"Final Score: {boards[b]['board'].calc_final_score(int(pick))}")
                return


def part2(verbose=False):
    input_file = "input.txt"
    data = read_input(input_file, verbose=verbose)

    N = 5  # Size of bingo board    
    chosen_nums = data[0].split(',') # Selected bingo numbers
    win_order = 0  # Tracks win order of boards
    last_pick = 0
    last_win = 0

    # Dict of bingo board objects
    boards = create_boards(data,N)

    # Find board that wins last
    for pick in chosen_nums:
        if verbose: print(f'Number {pick} chosen!')
        for b in boards:
            if boards[b]['win_order'] < 0 and boards[b]['board'].update(pick):
                boards[b]['win_order'] = win_order
                last_pick = pick
                last_win = win_order
                win_order += 1

    # Find last winning board
    last_win = win_order - 1
    for b in boards:
        if boards[b]['win_order'] == last_win:
            print(f'Board to win LAST, at number {last_win}')
            print(boards[b]['board'])
            print(f"Final score: {boards[b]['board'].calc_final_score(int(last_pick))}")


    


if __name__ == "__main__":
    try:
        part1(verbose=False)
        part2(verbose=False)
    except Exception as err:
        print(f'ERROR: {err}')