"""
Date: 8/14/20
12.1: Tower of Hanoi
"""

'''
Problem Statement: The Tower and Hanoi is a puzzle game with three rods and n disks, each a different size.
All the disks start off on the first rod in a stack. They are ordered by size, with the largest disk on the bottom
and the smallest one at the top. The goal of this puzzle is to move all the disks from the first rod to the last rod
while following these rules:
    1. You can only move on disk at a time
    2. A move consists of taking the uppermost disk from one of the stacks and placing it on top of another stack.
    3. You cannot place a larger disk on top of a smaller disk.
Write a function that prints out all the steps necessary to complete the Tower of Hanoi. You should assume that the
rods are numbered, with the first rod being 1, the second rod being 2, and the last rod being 3.

Example:
    n = 3
    Move 1 to 3
    Move 1 to 2
    Move 3 to 2
    Move 1 to 3
    Move 2 to 1
    Move 2 to 3
    Move 1 to 3
'''

'''                             My Solution                              '''
""" The way to solve this problem is that you need to move all but the bottom disk to the spare peg and then
move the bottom disk to the goal peg and then repeat this process until the problem is solved. """
def tower_of_hanoi(n: int, source='1', spare='2', goal='3') -> None:
    if n > 0:
        tower_of_hanoi(n-1, source, goal, spare) # Move n-1 disks to spare peg
        print(f'Move disk {n} from peg {source} to peg {goal}') # Move largest disk to goal
        tower_of_hanoi(n-1, spare, source, goal) # Move n-1 pegs from the spare peg to the goal peg


'''                             Test Cases                               '''
def main():
    tower_of_hanoi(4)

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Some times with recursive problems it is better to not think about them in terms of code because that can actually
        make it harder to think of the correct algorithm.
    * Always remember the to figure out the base case!
    * Work recursive problems out on paper to get a feel for how the recursion tree works.
'''

