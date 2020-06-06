"""
Date: 6/6/20
4.5: Reconstruct array using +/- signs
"""

'''
Problem Statement: The sequence [0,1,2, ..., N] has been jumbled and the only clue you have for its order is an array representing
whether each number is larger or smaller than the last. Given this info reconstruct an array that is consistent with it.
    Example: [None, +, +, _, +] could return [1,2,3,0,4]

'''
from typing import List
from collections import deque
'''                             My Solution                              '''
def reconstruct(info: List[str]) -> List[int]:
    # Create deque and fill it with numbers from 0...(N-1)
    deck = deque()
    for i in range(len(info)):
        deck.append(i)

    # Count "-" signs
    negatives = sum([1 if sign == "-" else 0 for sign in info])

    # For each negative sign pop top of deck off and put it on the back
    for _ in range(negatives):
        x = deck.popleft()
        deck.append(x)

    # Go threw signs and put either the top of stack for + or bottom for -
    return [deck.pop() if sign == "-" else deck.popleft() for sign in info]

'''                             Book Solution                            '''
def reconstruct_book(array):
    """ The idea of their solution is that every time you see the next sign is a negative sign you need
    to push the value you are at onto the stack to save it so you can go down for that negative. Then you
     move on to the next number and repeat and eventually when you see a + again you will put the value you
     are at in place and then put all the negatives in place. """
    answer = []
    n = len(array)-1
    stack = []

    for i in range(n):
        if array[i+1] == "-":
            stack.append(i)
        else:
            answer.append(i)
            while stack:
                answer.append(stack.pop())

    stack.append(n)
    while stack:
        answer.append(stack.pop())

    return answer

'''                             Test Cases                               '''
def main():
    print(reconstruct([None, "+", "+", "-", "+"]))
    print(reconstruct_book([None, "+", "+", "-", "+"]))

    print(reconstruct([None, "-", "-", "-", "+"]))
    print(reconstruct_book([None, "-", "-", "-", "+"]))

    print(reconstruct([None, "-", "-", "+", "+"]))
    print(reconstruct_book([None, "-", "-", "+", "+"]))



if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Using a deque allows you to be able to pull from either side easily
    * List comprehensions do shorted the code up alot
    * List comp then sum does take an additional pass so it a little slower
    * I like my solution better than books
'''

