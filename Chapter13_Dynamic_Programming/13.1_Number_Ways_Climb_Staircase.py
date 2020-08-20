"""
Date: 8/18/20
13.1: Number of Ways to Climb a Staircase
"""

'''
Problem Statement: There exists a staircase with n steps which you can climb up either 1 or 2 steps at a time. Given n,
write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
Example:
    n = 4
    :returns 5
    1,1,1,1
    2,1,1
    1,2,1
    1,1,2
    2,2

Follow-up: What if, instead of being able to climb 1 or 2 steps at a time you could climb any number from a set of positive
integers X? For example x = (1,3,5) and you can climb 1,3, or 5 steps at a time.
'''

'''                             My Solution                              '''
""" This seems like the same problem as the coin problem but calling it steps this time. So we can get to a step by either
taking one step from the previous step or two steps from two steps ago, then you solve all those sub problems and get the solution.
The major speed up here is that once you solve for a given n, you can just save its solution in a cache and look it up so
that you do not have to compute it again. This is a massive speed up especially for large values of n. Base cases are there is
only 1 way to get to 0 steps (dont take a step) and 1 way to get to 1 step (take a single step). Everything else can be solved
with the relationship step(n) = step(n-1) + step(n-2)."""

def count_ways_staircase(n: int, cache={0:1, 1:1}) -> int:
    assert n >= 0, "Negative steps can not be taken!"

    if n in cache:
        return cache[n]

    cache[n] = count_ways_staircase(n-1, cache) + count_ways_staircase(n-2, cache)
    return cache[n]

from typing import List
def count_ways_followup(n: int, options: List[int], cache={0:1, 1:1}) -> int:
    if n < 0:
        return 0

    if n in cache:
        return cache[n]

    cache[n] = sum(count_ways_followup((n-option), options, cache) for option in options)
    return cache[n]


'''                             Book Solution                            '''
def staircase(n, X):
    cache = [0 for _ in range(n+1)]
    cache[0] = 1

    for i in range(1, n+1):
        cache[i] += sum(cache[i-step] for step in X if i-step >= 0)

    return cache[n]

'''                             Test Cases                               '''
def main():
    assert count_ways_staircase(4) == 5
    assert count_ways_staircase(5) == 8
    assert count_ways_followup(5, [1, 3, 5]) == 5

if __name__ == '__main__':
    main()

'''
Lessons Learned:
    * These how many possible ways problems are a great place to use dynamic programming to cache results and use those
          cached results from subproblems to solve this problem. 
    * Bottom up works by using for loops instead of recursion to solve the problem.
    * Runtime is O(n*X) because for each n (1..n) you try each step combination. O(n) space to store all the results for each n.
'''

