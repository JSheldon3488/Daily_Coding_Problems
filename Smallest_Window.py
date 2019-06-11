# -*- coding: utf-8 -*-
"""
@author: Justin Sheldon
1.2: Locate smallest window to be sorted
"""

'''Problem Statement: Given an array of integers that are out of order, determine the bounds of the smallest possible window that
        must be sorted in order for the entire array to be sorted.
        Ex1. [3,7,5,6,9] will return (1,3). If you sort index's 1,2,3 the entire array will be sorted.
'''

'''                         My Solution                             '''
def shortestWindow(List):
    left = 0
    right = len(List) - 1 
    
    #Iterate over list moving left pointer as long as this element is the smallest element in the remaining list and therefore still in correct order
    smallest = True
    while smallest and left < len(List) - 1:
        if min(List[left:]) == List[left]:
            left+=1
        else:
            smallest = False
    
    #Iterate over the list moving the right pointer as long as the element is the largest in the remaining list.
    largest = True
    while largest and right > 0:
        if max(List[:right+1]) == List[right]:
            right-=1
        else:
            largest = False
    
    return(left,right)
    
    
    
'''                         Book Solution 1                             '''

def window(array):
    left, right = None, None
    s = sorted(array)
    
    for i in range(len(array)):
        if array[i] != s[i] and left is None:
            left = i
        elif array[i] != s[i]:
            right = i
    
    return left,right

''' Book Solution Notes: O(nlogn) Solution
1. This is O(nlogn) for the sort and then does another n iterations for the assigment
of left and right. My solution would have a better best case run time and probably a better
average case run time. If extremely large collection and partially sorted this algorithm
would outperform mine as my original algorithm would perform O(n^2).
2. Note that right doesnt just stop once it assigns it once. It checks all the way to the
end of the array which makes me think that starting from the end of the array and moving in
would save time.
'''


def window2(array):
    left,right = None, None
    n = len(array)
    max_seen, min_seen = -float("inf"), float("inf")
    
    #If this element is less then the max seen we know we have to shift the max seen to at least
    # this location therefore we set right to this location
    for i in range(n):
        max_seen = max(max_seen, array[i])
        if array[i] < max_seen:
            right = i
    
    #If this element is greater then the min seen then we know we have to shift the min seen
    # to at least this location therefore we set left = to this location
    for i in range(n-1, -1, -1):
        min_seen = min(min_seen, array[i])
        if array[i] > min_seen:
            left = i
    
    return left,right

'''Book Solution Notes: O(n) Solution
1. Always try to think of a solution using a running max and min like this if it is applicable
This will likely speed up your algorithm to constant time because you only have to loop threw the
container once. (twice in this example... still O(n)).
2. This algorithm is the most efficient but as usual it is a little more complex to understand what
is happening. There is usually a trade off between simplicity and speed. (not always) 
'''


'''                           Test Cases                                  '''
def main():
    list1 = [3, 7, 5, 6, 9]
    print(shortestWindow(list1) == (1, 3))
    list2 = [6, 5, 3, 7, 9]
    print(shortestWindow(list2) == (0, 2))
    list3 = [6, 5, 9, 3, 7]
    print(shortestWindow(list3) == (0, 4))


if __name__ == '__main__':
    main()


'''
Lessons Learned:
    *Starting from the end of an array and working backwards can save some iterations
    *Always try to think of a solution using a running max and min like this if it is applicable. This will likely speed up
     your algorithm to constant time because you only have to loop threw the container once.
     *-float("inf"), float("inf") will give you the smallest and largest possible floats in Python
'''





