"""
Date: 7/2/19
3.4: Find Intersecting Nodes of Linked List
"""

from Singly_Linked_List import Singly_Linked_List as LL

'''
Problem Statement: Given two singly linked lists that intersect at some point, find the inersecting node. Assume the lists are non-cyclical
    Ex. A = 3 --> 7 --> 8 --> 10
        B = 99 --> 1 --> 8 --> 10
        Returns Node(8)
    Do this in O(m+n) time where m and n are the lengths of the lists

'''

'''                             My Solution                              '''
def intersecting_nodes(A,B):
    """
    Finds the first intersecting node of the two Linked Lists inputs.

    :param A: Linked List of Nodes
    :param B: Linked List of Nodes
    :return: The first intersecting node found in A and B. Throws exception if no intersecting Nodes
    """
    #Creating a dictionary and storing all the data in it from 1 of the linked lists
    dict = {}
    current = A.head
    while current != None:
        dict[current.data] = 1
        current = current.next

    #If this data already exists in dictionary return this node else move on to next Node
    current = B.head
    while current!= None:
        if current.data in dict:
            return current
        current = current.next

    raise ValueError("No intersecting Nodes!")
'''Notes:
    * Dictionaries are O(1) for in check because they use hashing so this is O(n+m).
    * When checking for uniqueness between two containers putting them into a hash table (dictionary) is a efficient way to do it.
'''



'''                             Book Solution                            '''
def intersection(a,b):
    m,n = a.size(), b.size()
    cur_a, cur_b = a.head,b.head

    if m > n:
        for _ in range(m-b):
            cur_a = cur_a.next
    else:
        for _ in range(n-m):
            cur_b = cur_b.next

    while cur_a.data != cur_b.data:
        cur_a = cur_a.next
        cur_b = cur_b.next

    return cur_a


'''                             Test Cases                               '''
def main():
    A = LL()
    A.insert(3), A.insert(7), A.insert(8), A.insert(10)
    print(A)
    B = LL()
    B.insert(99), B.insert(1), B.insert(8), B.insert(10)
    print(B)
    print(intersecting_nodes(A,B))

if __name__ == '__main__':
    main()


'''
Lessons Learned:
    * I didn't know that the Nodes had to be in the same location in the Lists. Well defined problems make all the difference. This 
        Problem was defined poorly. Always try to define your problem and code as explicitly as possible.
    * If you need to loop over something but dont actually need the variable use _ to signify this in your code instead of i.
'''
