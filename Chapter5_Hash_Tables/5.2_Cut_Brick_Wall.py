"""
Date: 6/12/20
5.2: Cut Brick Wall
"""

'''
Problem Statement: A wall consists of several rows of bricks of various integer lengths and uniform height.
Your goal is to find a vertical line going from the top to the bottom of the vall that cuts through the fewest number
of bricks. If the line goes through the edge between two bricks this does not count as a cut.

Example: [ [3,5,1,1],
           [2,3,3,2],
           [5,5],
           [4,4,2],
           [1,3,3,3],
           [1,1,6,1,1] ]
           
Solution: Cut through the 8th brick because there is a break point there in rows 1,2,4,6 so we only make two cuts.
'''

'''                             My Solution                              '''
""" So essentially it looks like you just need to find the max breakpoints. We know all the lists will add up to the same value (its height)
and so if we create a hash map where each time we see a break point we just +1 to that given break point and then keep track of the max or
find the max in the hash map at the end we can solve this.
For each row there is multiple break points. for example row one has breakpoints 3,8,9. Gotta make sure not to do the last value because that
value will be the same for all rows. So for each row we calculate a running sum and use it as a key into the hashmap and +1 each time.
"""
from typing import List
from collections import defaultdict

def cut_brick_wall(lengths: List[List[int]]) -> int:
    breakpoints = defaultdict(int)
    for l in lengths:
        breakpoint = 0
        for index in range(len(l)-1):
            breakpoint += l[index]
            breakpoints[breakpoint] += 1

    max_breakpoint = max(breakpoints, key= lambda x: breakpoints[x])
    return max_breakpoint

'''                             Book Solution                            '''
def fewest_cuts(wall):
    cuts = defaultdict(int)

    for row in wall:
        length = 0
        for brick in row[:-1]:
            length += brick
            cuts[brick] += 1

    return len(wall) - max(cuts.values())


'''                             Test Cases                               '''
def main():
    assert cut_brick_wall([[3,5,1,1],
                            [2,3,3,2],
                            [5,5],
                            [4,4,2],
                            [1,3,3,3],
                            [1,1,6,1,1]]) == 8

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Can get the max of a dictionary using the max function and a lambda function for the key to get the value at that key
        ** This will return the key with the max value not the max value
    * The actual value supposed to be returned was the fewest number of cuts. So if you know how many rows have a given break point
    you can just take num rows - how many rows have break point and get the solution
    * We had same algorithm but their Python is better than mine
    * I like their naming of wall and row and brick instead of lengths,l, breakpoint. I actually like breakpoint more than brick but wall and row
    are much better than lengths and l
    * If you want all but the last thing in a list use slicing instead of range!!! list[:-1] will give you everything but the last and then 
    it cleans up the future code without all the indexing.
    * Use slicing, try to name your variables better, and read the problem carefully to make sure you are returning the correct thing.
'''

