"""
Date: 6/11/19
1.4: Find number of smaller elements to the right
"""
import bisect


'''
Problem Statement: given an array of integers, return a new arrray where each element in the new array is the number of smaller
    elements to the right of that element in the original input array.
    Ex1. [3,4,9,6,1] returns [1,1,2,1,0]
'''

'''                     My Solution                             '''
def countSmallertoRight(List):
    countArray = []
    for i in range(len(List)):
        count = 0
        for j in range(i+1,len(List)):
            if List[i] > List[j]:
                count+=1
        countArray.append(count)
    return countArray
'''Note: This solution works, but it is O(n^2). I assume there is a faster method so I am going to try some stuff below in a
        second solution before checking the books answers.
'''

def fasterCountSmallertoRight(List):
    #Start with the rightmost element already accounted for
    countArray = [0]
    sorted_seen = [List[-1]]

    #find correct index in sorted_seen, update countArray with result, updated sorted_seen with new element in correct position
    for i in range(len(List) -2, -1, -1):
        sortedIndex = findSortedIndex(sorted_seen, List[i])
        countArray.insert(0,sortedIndex)
        sorted_seen.insert(sortedIndex,List[i])
    return countArray

def findSortedIndex(sorted_seen, currentElement):
    index = 0
    for ele in sorted_seen:
        if ele > currentElement:
            break
        else:
            index+=1
    return index
'''Notes: 
    *Tried seeing if there was some combination of the previous answer that would help with the current count but it does
    not because you dont know the difference in magnitude between the current element and the last element.
    *Trying opposite problem "larger elements to the right" and then subtracting length of list works but would still be O(n^2)
    *Working from the back of the array and seeing where the element will end up in a sorted list will tell you how many smaller elements there
    are to that elements right. (You have to start from the back of the list)
'''

'''                     Book Soltuions                          '''

def smaller_counts_naive(List):
    result = []
    for i, num in enumerate(List):
        count = sum(val < num for val in List[i+1:])
        result.append(count)
    return result

'''Notes: 
    * enumerate() returns a object with an index and the data value (index,datavalue) then you can use either the data and/or the index
        Note: The start is set to 0 for the index's but you can set them to whatever you want
    * sum(val < num for val in List[i+1:]) is a generator expression, more below in lessons learned.
'''

def smaller_counts(List):
    result = []
    seen = []

    for num in reversed(List):
        i = bisect.bisect_left(seen,num)
        result.append(i)
        bisect.insort(seen,num)

    return list(reversed(result))

'''Notes: 
    * time complexity of reversed is O(n)
    * the bisect class is used to maintain a sorted collection without having to sort after each insertion
    * bisect.bisect_left() will return the index where the element should be inserted and will put it to the left in case of ties
        (essentially a better version of my findSortedIndex() above)
    * bisect.insort() will insert an element into the list in sorted order for you. Runs .bisect() then an insert.
        the inerstion step is O(n).
'''

'''                     Test Cases                              '''
def main():
    ex1 = [3,4,9,6,1]
    print(countSmallertoRight(ex1) == [1,1,2,1,0])
    print(fasterCountSmallertoRight(ex1) == [1,1,2,1,0])


if __name__ == '__main__':
    main()


'''
Lessons Learned:
    * Generator Expressions are extremely powerful, easy to read, and easy to understand. Below are some cool examples from the Python Docs
        Ex. unique_words = set(word  for line in page  for word in line.split()) Notice that multiple loops are allowed
        Ex. sine_table = dict((x, sin(x*pi/180)) for x in range(0, 91)) You can use this in a lot of different functions like sum(), dict(),
        list(), max(), set(), ect.
    * enumerate(iterable) is useful if you need an index and the value from the iteration.
    * The bisect class is useful when you want to find an index where an item should be inserted into an already sorted list or you
        want to insert an item into an already sorted list. You could do all these things manually like I did above but it is much
        easier to just use a single method from the class bisect.
    * It appears common practice in Python is to use _ instead of camel case.
'''
