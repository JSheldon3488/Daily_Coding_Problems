"""
Date: 8/21/20
13.3 Painting Houses
"""

'''
Problem Statement: A builder is looking to build a row of n houses that can be of k different colors. She has a goal of minimizing
cost while ensuring that no two neighboring houses are the same color.

Given an n by k matrix where the entry at the ith row and jth column represents the cost to build the ith house with the
jth color, return the minimum cost require to achieve this goal.

Example:
    n=5, k=3 (rows are cost to build house, col is color)
    [[5, 4, 3],
     [4, 6, 3],
     [2, 1, 4],
     [2, 2, 2],
     [4, 5, 3]]
    :returns 13   path (3,1,2,1,3) or (2,3,2,1,3)
'''

'''                             My Solution                              '''
""" So looking at the example above we need to consider the one constraint and that is that no two houses can be the same color.
Therefore if we select the cheapest house in a row we need to consider the two rows that are adjacent to it. This feels like the rob the
houses problem but can not rob two people that are next to each other. Okay lets try to break this down step by step. One thing to consider
is when would we ever pick the non greedy solution at this step? When choosing greedy solution now leads to having to choose a combination with the
next houses that would lead to a worse outcome.

    Single house: Pick best solution (but may need to store other information)
    Two Houses: Pick min(color1+min(c2,c3), color2+min(c1,c3), c3+min(c1,c2)) 
    Three Houses: Pick min(c1+min(th_c2,th_c2), c2+min(th_c1,th_c3), c3+min(th_c1,th_c2))      
    ...
    return min(c1,c2,c3)
    
    I think this will work where we just keep track of three values for each previous layer. I will work it out on the example above and see if this works.
    house1 = (5,4,3)
    house2 = (4+3, 6+3, 3+4) = (7,9,7)
    house3 = (2+7, 1+7, 4+7) = (9,8,11)
    house4 = (2+8, 2+9, 2+8) = (10,11,10)
    house5 = (4+10, 5+10, 3+10) = (14,15,13)
    So min would be 13 and optimal path would be choose [3, 1, 2, 1, 3]
"""
from typing import List
def painting_houses(house_color_matrix: List[List[int]]) -> int:
    prev_sum = [0]*len(house_color_matrix[0])

    for house in house_color_matrix:
        tmp = [0]*len(house)
        for color, cost in enumerate(house):
            tmp[color] = cost + min(prev_sum[:color]+prev_sum[color+1:])
        prev_sum = tmp

    return min(prev_sum)

'''                             Book Solution                            '''
def build_houses(matrix):
    k = len(matrix[0])
    solution_row = [0]*k

    for r, row in enumerate(matrix):
        new_row = []
        for c, val in enumerate(row):
            new_row.append(min(solution_row[i] for i in range(k) if i != c)+val)
        solution_row = new_row

    return min(solution_row)

'''                             Test Cases                               '''
def main():
    houses_cost_lists = [[5, 4, 3],
                        [4, 6, 3],
                        [2, 1, 4],
                        [2, 2, 2],
                        [4, 5, 3]]
    assert painting_houses(houses_cost_lists) == 13

    houses_cost_lists = [[5, 4, 3, 2, 1],
                        [4, 6, 3, 5, 3],
                        [2, 1, 4, 3, 3],
                        [2, 2, 2, 4, 6],
                        [4, 5, 3, 1, 2]]
    print(painting_houses(houses_cost_lists))

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * Always try to run through an example and catch all the correct questions you should be asking right away and all the
        details and complexities of this problem that you need to solve. Here once i ran through the example and asked myself
        the correct questions instead of trying to solve the entire thing right away I came to the correct solution.
    * Do not get too stuck on your example! Here I forgot to remember that it is k different colors and I hard coded k=3
        for my solution! That being said it is the correct logic!
    * Another way to get min of a list without a certain index in it is to use a comprehension where you check if i != j.
        This might actually be quite a bit slower than slicing but not all languages support slicing like Python.
'''

