"""
Date: 6/13/19
1.1: Get product of all other elements
"""

'''
Problem Statement: Given an array of integers, return a new array such that each element at index i of the new array is the product of
    all the numbers in the original array except the one at i.
    Ex1. [1,2,3,4,5] returns [120, 60, 40, 30, 24]
    Ex2. [3,2,1] returns [2,3,6]
'''

'''                             My Solution                             '''

def productAllOther(List):
    output = []
    for i in range(0,len(List)):
        product = 1
        for ele in List:
            product *= ele
        output.append(product//List[i])
    return output


def prodAllOtherNoDiv(List):
    # Same problem solved without using Division
    output = []
    current = 0
    for i in range(0, len(List)):
        product = 1
        for j in range(0, len(List)):
            if current != j:
                product *= List[j]
        output.append(product)
        current += 1
    return output
'''Notes:
    * Both of these solutions are O(n^2) and get the job done but nothing really fancy
'''


'''                              Book Solutions                      '''

def productsPrefixSufix(nums):
    prefixProducts = []
    for num in nums:
        #This will just return true if len > 1. I like len(x) > 0 because it is more explicit
        if prefixProducts:
            prefixProducts.append(prefixProducts[-1] * num)
        else:
            prefixProducts.append(num)
    # Example of a Prefix Product for [1,2,3,4] = [1,2,6,24] 
    
    suffixProducts = []
    # reversed will reverse an array list for you
    #suffix product is the same as prefix just working from the back of the list
    # Example [1,2,3,4] = [4,12,24,24]
    for num in reversed(nums):
        if suffixProducts:
            suffixProducts.append(suffixProducts[-1] * num)
        else:
            suffixProducts.append(num)
    suffixProducts = list(reversed(suffixProducts))
    
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffixProducts[i+1])
        elif i == len(nums)-1:
            result.append(prefixProducts[i-1])
        else:
            result.append(prefixProducts[i-1] * suffixProducts[i+1])
    
    return result
'''Notes:
    * This solution is O(n) and does beat my solution. A little more complex in terms of the code but much faster.
'''


'''                             Test Cases                              '''
def main():
    list1 = [1,2,3,4,5]
    list2 = [3,2,1]
    print(productAllOther(list1) == [120, 60, 40, 30, 24])
    print(productAllOther(list2) == [2, 3, 6])
    print(prodAllOtherNoDiv(list1) == [120, 60, 40, 30, 24])
    print(prodAllOtherNoDiv(list2) == [2, 3, 6])
    print(productsPrefixSufix(list1) == [120, 60, 40, 30, 24])
    print(productsPrefixSufix(list2) == [2, 3, 6])
    

if __name__ == '__main__':
    main()


'''
Lessons Learned:
    * Name your list objects exactly what they are instead of just List. It gives you more information for the same cost
    * Its really useful to check the corner cases first,  Non-corner case can then just be the else case
    * Always try to think of a clever way to combine results to get what you are after instead of just the basic straight
        forward O(n^2) type methods.
'''
