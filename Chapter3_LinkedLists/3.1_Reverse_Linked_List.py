"""
Date: 6/19/19
4.1: Reverse Linked List
"""

'''
Problem Statement: Given the head of a singly linked list, reverse it in-place.
    Ex. [1,2,3,4] returns [4,3,2,1]
    
'''
'''Node Class used to represent a single linked list'''
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

    # Override print method so that we can see the entire linked list to check our results
    def __str__(self):
        s = "[" + str(self.data)
        current = self.next
        while current != None:
            s += ", " + str(current.data)
            current = current.next
        s += "]"
        return s

'''                             My Solution                              '''
def reverse_LinkedList(head):
    #Single Node not a Linked List
    if head.next == None:
        return head

    #Multiple Nodes need to reverse the List
    previous = None
    current = head
    while current != None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    #All pointers have be reassigned and current is None so return previous as the new head
    return previous


'''                             Book Solution                            '''
def reverse(node):
    head, _ = _reverse(node)

def _reverse(node):
    if node is None:
        return None,None

    if node.next is None:
        return node,node

    head, tail = _reverse(node.next)
    node.next = None
    tail.Next = node
    return head,node

'''                             Test Cases                               '''
def main():
    Ex1 = Node(1)
    print(reverse_LinkedList(Ex1))
    Ex1.next = Node(2)
    Ex1.next.next = Node(3)
    Ex1.next.next.next = Node(4)
    print(reverse_LinkedList(Ex1))


if __name__ == '__main__':
    main()


'''
Lessons Learned:
    * Initializing the previous node to None was the part I was missing
    * Order of the way you do assigments matters a lot in this problem, be careful and draw out examples
    * _ is used to denote an unused variable
    * When you want to update a collection as you traverse threw it always try to think of using two pointers
'''
