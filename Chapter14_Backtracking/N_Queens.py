"""
Date: 8/24/20
N Queens Problem
"""

'''
Problem Statement: This problem is introduced at the beginning of the chapter to introduce backtracking. I want to see 
a solution and explanation for this problem but I think that the books solution and explanation is terrible. So I am going
to look around on the internet and post the solution and lessons learned here.

The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.
Example: 
    n = 4
    :returns  { 0,  1,  0,  0}
              { 0,  0,  0,  1}
              { 1,  0,  0,  0}
              { 0,  0,  1,  0}

Notice here that no two queens (represented as 1's) could attack each other in chess.

Base case is that all queens are replaced and we can return true (check a valid solution)
For all rows in the current column try to place a queen in this row,column, if it is valid then recursively try to
solve the problem from here. if placing that queen lead to a solution base case will return true. If placing queen doesnt
lead to a solution then unmark this row,column (backtrack) and go to the next row. If all rows were tried return flase
to trigger backtracking to move on to the next column.
'''

global N
N = 4

def print_solution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

def is_safe(board, row, col):
    """A utility function to check if a queen can be placed on board[row][col]. Note that this function is called when
    "col" queens are already placed in columns from 0 to col -1. So we need to check only left side for attacking queens.
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queen_util(board, col):
    # base case: If all queens are placed then return true
    if col >= N:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            # recur to place rest of the queens
            if solve_n_queen_util(board, col + 1):
                return True
            # If placing queen in board[i][col] doesn't lead to a solution, then backtrack remove queen from board[i][col]
            board[i][col] = 0

    # if the queen can not be placed in any row in this column col then return false
    return False


def solveNQ():
    """
    This function solves the N Queen problem using Backtracking. It mainly uses solve_n_queen_util() to solve the problem.
    It returns false if queens cannot be placed, otherwise return true and placement of queens in the form of 1s.
    note that there may be more than one solutions, this function prints one of the feasible solutions.
    """
    board = [[0]*N for i in range(N)]

    if not solve_n_queen_util(board, 0):
        print("Solution does not exist")
        return False

    print_solution(board)
    return True


'''                             Test Cases                               '''
def main():
    solveNQ()

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Saw a trick bug here. If I create a row then put that row in with a list comprehension like so [row for i in range(N)] then
        all the rows in the board will point to the same thing! row here is a reference to the underlying List so I just pass
        in 4 references instead of 4 lists.
    * It seems like these back tracking recursive solutions hinge on you popping off the previous solution at the right time
        after that path did not lead to a solution.
    
'''

