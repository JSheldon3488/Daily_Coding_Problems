# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:44:27 2019
@author: Justin Sheldon
Chapter 1.3: Calculate maximum subarray sum
"""

'''
Problem Statement: Given an array of numbers, find the maximum sum of any contiguous subarray of the array. Try to solve in
O(n) time.
    Ex. [34,-50, 42,14,-5,86] max sum = 137 and would be the elements 42,14,-5,86.
    Ex2. [-5,-1,-8,-9] max sum = 0.
'''
def max_SubarraySum(List):
    max = current_max = 0
    for value in List:
        current_max += value
        if current_max > max:
            max = current_max
        if current_max < 0:
            current_max = 0
    return(max)


'''
Follow Up Problem: Now what if the elements can wrap around?
    Ex. [8,-1,3,4] max sum = 14 and we choose 3, 4, 8
    Note: Definition of this problem is confusing because obviously if we could wrap around forever we would just sum
        the array forever. Let's assume the max length of the subarray is the length of the array.
    Note: Could not figure this one out! The trick is to subtract the minimum subarray from the entire array sum which
    will represent the max wrap around subarray. Also remember you need to calculate the original max subarray because that
    could still be greater then the wraparound max subarray.
'''
def wrapAround_maxSubArraySum(List):
    #Find min Subarray
    min_subArray = current_min = total_sum = 0
    for value in List:
        total_sum += value
        current_min +=  value
        if current_min < min_subArray:
            min_subArray = current_min
        if current_min > 0:
            current_min = 0

    return(max(total_sum - min_subArray, max_SubarraySum(List)))




'''                                             Book Solutions                                                       '''

def book_max_subArraySum(List):
    max_ending_here = max_so_far = 0
    for x in List:
        max_ending_here = max(x, max_ending_here+x)
        max_so_far = max(max_ending_here,max_so_far)
    return max_so_far

'''
Book Solution Notes: 
    *max_ending_here will reset to just x if the sum before it went negative, I did this manually by just setting sum to 0
'''

def book_max_circular_subarry(arr):
    max_sub_sum_wrap = sum(arr) - min_subarray_sum(arr)

    return max(book_max_subArraySum(arr), book_max_circular_subarry())

def min_subarray_sum(arr):
    min_ending_here = min_so_far = 0
    for x in arr:
        min_ending_here = min(x, min_ending_here +x)
        min_so_far = min(min_ending_here,min_so_far)

    return min_so_far

'''
Book Solution Notes: 
    *If you can't solve a problem try solving the opposite problem and then using that solution to solve the original problem
    *Not a huge difference but it seems wasteful to calculate the sum() and then the min subarray seperately when you are going to be
    iterating over the list anyways so you might as well calculate the sum at the point in time. Still same O() runtime but an entire
    iteration of the list faster.
'''


def main():
    #Original Problem
    Ex1 = [34,-50, 42,14,-5,86]
    print(max_SubarraySum(Ex1) == 137)
    Ex2 = [-5,-1,-8,-9]
    print(max_SubarraySum(Ex2) == 0)

    #Follow up Problem
    Ex3 = [8,-1,3,4]
    print(wrapAround_maxSubArraySum(Ex3) == 15)
    print(wrapAround_maxSubArraySum(Ex1) == 171)
    print(wrapAround_maxSubArraySum(Ex2) == 0)

if __name__ == '__main__':
    main()

'''
Lessons Learned: 
    *If you are really stumped on a problem try to see if you can solve the opposite problem and use the solution
    to the opposite problem to help you solve the original problem.
'''