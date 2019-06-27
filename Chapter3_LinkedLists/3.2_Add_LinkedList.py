"""
Date: 6/26/19
3.2: Add two linked lists that represent numbers
"""

'''
Problem Statement: We can represent an integer in a linked list format by having each node represent a digit in the number.
    The nodes are connected in reverse order, such that the number 54321 is represented by the following liked list:
        1 --> 2 --> 3 --> 4 --> 5
    Given two linked lists in this format, return their sum.
    Ex:
        9 --> 9
        5 --> 2
        Returns:
        4 -- > 2 --> 1

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

    def size(self):
        res = 1
        while self.next != None:
            res += 1
            self = self.next
        return res


'''                             My Solution                              '''
def sum_linkedList(A,B):
    """
    Parameters:
        A (Linked List): where the linked lists represent an integer with each individual digit a node. Represented in reverse order so 25 is 5 --> 2.
        B (Linked List): Same representation as A

    Returns:
        The sum of the two integers A and B represented as a linked list. (again in reversed order)
    """
    # Because we are only using a node and not a true linked list we will have to initialize a node to None in the start and use that as head
    head = current = Node(None)
    sum = 0
    remainder = 0
    carry = 0

    for i in range(max(A.size(), B.size())):
        #Lists could be different sizes so want to make sure there is actual data in this node
        if A != None:
            sum += A.data
            A = A.next
        if B != None:
            sum += B.data
            B = B.next
        remainder = sum%10
        carry = (sum - remainder)//10
        # Need to handle first node slightly different then the rest
        if current.data == None:
            current.data = remainder
        else:
            current.next = Node(remainder)
            current = current.next
        # Set sum for next iteration depending on carry value
        sum = carry

    # Last Node if carry was 1
    if carry > 0:
        current.next = Node(carry)

    return head


'''                             Book Solution                            '''
def add(node0, node1, carry =0):
    if not node0 and not node1 and not carry:
        return None

    node0_val = node0.data if node0 else 0
    node1_val = node1.data if node1 else 0
    total = node0_val + node1_val + carry

    node0_next = node0.next if node0 else None
    node1_next = node1.next if node1 else None
    carry_next = 1 if total >= 10 else 0

    return Node(total%10, add(node0_next, node1_next, carry_next))

'''Notes:
    * Nice inline if else statements that I can use in future code to set values
    * I hate the name of this function! It does not tell you what is really happening and could easily be mistaken for a
        built in function that is part of Python.
    * Need to start thinking of how to solve more things recursively
    * 
'''

'''                             Test Cases                               '''
def main():
    # Book Example
    A = Node(9,Node(9))
    B = Node(5,Node(2))
    print(sum_linkedList(A,B))
    print(add(A,B))
    # Example with different length Lists

    C = Node(4,Node(2,Node(1,Node(5))))
    D = Node(6,Node(7))
    print(sum_linkedList(C,D))
    print(add(C,D))


if __name__ == '__main__':
    main()


'''
Lessons Learned:
    * When you are not sure if your value will be a Node or None do not check Node.data or Node.next because it could be NoneType instead and
        you code will crash trying to access a attribute on NoneType which doesnt exist. Instead use check like A != None
    * Having an actual Linked List class probably would have made more sense and resulted in cleaner code
    * There is a way to do a nice inline if else condtion     node0_val = node0.data if node0 else 0
    * Never name your functions something that could be confused with Python built-ins!
'''