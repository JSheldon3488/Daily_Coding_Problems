"""
Date: 8/26/20
14.2: Solve Sudoku
"""

'''
Problem Statement: Sudoku is a puzzle where you are given a 9 by 9 grid partially filled with digits. The objective is
to fill the grid subject to the constraint that every row, column, and box (3x3) must contain all of the digits 1 to 9. 
'''

'''                             My Solution                              '''
""" I don't think I have ever actually played a full game of sudoku in my life. My first question is can you solve one
board at a time and if the board is solved you know you are good? Or does it depend on the other boards, like for example
you solve the top left sub board and then find out when you move on to the next board that that solution will not work and
you have to backtrack and resolve the first sub-board, or once you solve a sub-board its good and you can move on knowing
that you are fine? Okay so you can not guarantee that the board is finished when you fill it in. As you move to other boards
it might be that you choose the wrong solution for the previous board and have to backtrack. This is actually a pretty
good backtracking problem but it seems like a MASSIVE search tree with a little bit of pruning to me.
This is basically an impossible problem to solve without knowing how the Sudoku puzzle stored in memory. Is this a class
object with some board attributes or just a List of Lists of Lists? Its impossible to know here so I will just
solve this problem the best I can with a pseudo-code algorithm and then see the real solution. The biggest issue I am having
in my mind right now is that how does the algorithm know where to backtrack to? I guess as soon as there is no more options to
try it will back track to the last place it was. So you make a guess that is valid, move forward to a sub problem where this
guess is filled in, make a valid guess for the next subproblem... and on until you hit a dead end then you back track to the
last valid solution and try a different guess. I think each square will have to have a list of valid guesses then and
when you make a guess you remove it from the list. """

"""
def sudoku_solver(board, ?)
    square = Find first avail empty square
    valid_options = Create a valid options list (Need to check valid in mini square, valid in row, and valid in col)
    
    loop over valid options:
        Place one of the valid options in square and remove it from valid_options
        if check_game_solution:
            return solved game
        else call sudoku_solver(updated_board)
        We returned to this point without a solved solution so we know this option is not good so remove it from the board

    Return Board. We got here because all valid options for this square do not work, we need to backtrack a layer to the 
    last move and try his next valid option. Eventually we will get the correct solution...
        (Do we actually need to return board here?) Yes but little confused on what will be passed back up the call stack.
    
So I could implement this with the given data structure to represent sudoku, the util functions find_first_empty(), 
check_valid_row(), check_valid_col(), check_valid_box(), check_game_solved() and I think that is it. I might actually
build this later with a real Sudoku class and built in solver.
"""



'''                             Book Solution                            '''
EMPTY = 0

def sudoku(board):
    if is_complete(board):
        return board

    r, c = find_first_empty(board)

    for i in range(1,10):
        board[r][c] = i
        if valid_so_far(board):
            result = sudoku(board)
            if is_complete(result):
                return result
        board[r][c] = EMPTY

    return board

def is_complete(board):
    return all(all(val is not EMPTY for val in row) for row in board)

def find_first_empty(board):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == EMPTY:
                return i,j

def valid_so_far(board):
    if not rows_valid(board):
        return False
    if not cols_valid(board):
        return False
    if not blocks_valid(board):
        return False
    return True

def rows_valid(board):
    for row in board:
        if duplicates(row):
            return False
    return True

def cols_valid(board):
    for j in range(len(board[0])):
        if duplicates([board[i][j] for i in range(len(board))]):
            return False
    return True

def blocks_valid(board):
    for i in range(0,9,3):
        for j in range(0,9,3):
            block = []
            for k in range(3):
                for l in range(3):
                    block.append(board[i+k][j+l])
            if duplicates(block):
                return False
    return True

def duplicates(arr):
    c = {}
    for val in arr:
        if val in c and val is not EMPTY:
            return True
        c[val] = True
    return False

'''                             Test Cases                               '''



def main():
    return

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * This is a great example of a backtracking problem BUT there problem statement was terrible! They should have exalpined that
    the sudoku board would be represented as a list of list where each inner list is the row. Without that information how
    in the world could you go about writing code to solve this problem?
    * Sometime you can just write the core algorithm and then make note of all the utility functions you will need to
        solve the problem. The utility functions are just questions like row_valid? ect.
    * Always remember to think about what you will be returning up the call stack because you have to return something! 
        Otherwise your call stack will unwind and you will get None returned.
'''

