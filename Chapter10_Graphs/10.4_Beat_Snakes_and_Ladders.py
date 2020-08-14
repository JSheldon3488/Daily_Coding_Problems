"""
Date: 8/10/20
10.4: Beat Snakes and Ladders
"""

'''
Problem Statement: Snakes and Ladders is a game played on a 10x10 board, the goal of which is get from square 1 to square 100.
On each turn players will roll a six-sided die and move forward a number of spaces equal to the dice roll. If they land on a square
that represents a snake or ladder they will be transported ahead or behind, respectively, to a new square.
Find the smallest number of turns it takes to beat snakes and ladders.
Example:
    snakes = {17: 13, 52: 29, 57: 40, 62: 22, 88: 18, 95: 51, 97: 79}
    ladders = {3: 21, 8: 30, 28: 84, 58: 77, 75: 86, 80: 100, 90: 91}
'''

'''                             My Solution                              '''
""" The board is static which means all that matters is the rolls and how many you make. This seems like a problem that could
be solved in parallel but that is not what they are looking for here. This seems like a BFS graph problem I am just wondering
if there is any way to prune the search space to make it smaller as you go. I think if you try all 6 moves and only store the
best non snake non ladder move and then any ladder moves you will prune the search space and get to the optimal solution.
The reason I think you need to still store the best move that is not a ladder is because a ladder could lead you past the
best ladder in the game and then you would miss it. Where if you store the best move and all ladder moves you will not miss
any really good ladders because you always have a path progressing linearly through the board. Also not that we need to put on the
queue and pop off in layers so that we can keep track of a move count and return as soon as any path finishes."""
from _collections import deque
from typing import Dict


def optimal_snakes_ladders(snakes: Dict, ladders: Dict) -> int:
    queue = deque()     # (space, turn)
    queue.append((1, 0))
    best_seen = None

    while queue:
        turn = queue.popleft()
        found_max_linear = False
        for roll in range(6, 0, -1):
            next_square = turn[0] + roll
            next_turn = turn[1] + 1

            # Dont process turns past the end of the board
            if next_turn > 100:
                continue

            # Figure out if we reached the end
            if next_square == 100 or ladders.get(next_square) == 100:
                return next_turn

            # Find largest possible role that is not a snake
            if not found_max_linear and not snakes.get(next_square):
                if ladders.get(next_square):
                    next_square = ladders.get(next_square)
                queue.append((next_square, next_turn))
                found_max_linear = True

            # Find all ladder rolls
            elif ladder_result := ladders.get(next_square):
                queue.append((ladder_result, next_turn))

    return best_seen

'''                             Book Solution                            '''

'''                             Test Cases                               '''


def main():
    snakes = {17: 13, 52: 29, 57: 40, 62: 22, 88: 18, 95: 51, 97: 79}
    ladders = {3: 21, 8: 30, 28: 84, 58: 77, 75: 86, 80: 100, 90: 91}
    print(optimal_snakes_ladders(snakes, ladders))


if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * When you do DFS and are looking for a minimum like this, then the first solution you come across will be the minimum.
    * When doing DFS on a graph that you could end up processing the same node more than once like in this game it is best
        to use a visited dictionary so that you only process a node once. For example in this case you get to 84 multiple
        times from different paths because of that big ladder and therefore process it more than you need to.
'''
