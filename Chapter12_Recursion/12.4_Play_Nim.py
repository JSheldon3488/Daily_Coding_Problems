"""
Date: 8/17/20
12.4: Play Nim
"""

'''
Problem Statement: The game of Nim is played as follows. Starting with three heaps, each containing a variable number
of items, two players take turns removing one or more items from a single pile. The player who eventually is forced
to take the last stone loses.
Example:
    heap sizes: 3,4,5
    player 1 takes 3 from B
    3,1,5
    player 2 takes 2 items from C
    3,1,3
    player 1 takes 3 items from A
    0,1,3
    player 2 takes 3 items  from C
    0,1,0
    player 1 takes 1 item from A and loses

Given a list of non-zero starting values [a,b,c] and assuming optimal play, determine whether the first player has a forced win.
'''

'''                             Book Solution                            '''
def update(heaps, pile, items):
    heaps = list(heaps)
    heaps[pile] -= items
    return tuple(heaps)

def get_moves(heaps):
    moves = []
    for pile, count in enumerate(heaps):
        for i in range(1, count + 1):
            moves.append(update(heaps, pile, i))

def nim(heaps):
    if heaps == (0, 0, 0):
        return True

    return any([nim(move) != True for move in get_moves(heaps)])


def nim_constant(heaps):
    a,b,c = heaps
    if a == b == c == 1:
        return False
    return a ^ b ^ c != 0


'''                             Test Cases                               '''


def main():
    return


if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Usually in 2 player games some form of minimax will be used to find the optimal solution
    * Some problems just have a math trick solution that is not really that helpful for coding practice or learning imo.
        Knowing that a losing state has an Xor product of 0 does not really help you with any other problems besides nim.
    * I guess the big takeaway from this problem is that xor in Python is ^
'''
