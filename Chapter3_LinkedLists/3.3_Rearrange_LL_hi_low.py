"""
Date: 6/14/19
2.2: Generate Palindrome Pairs
"""

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

'''
Problem Statement: Given a linked list, rearrange the node values such that they appear in alternating low --> high order.
    * I think we can assume the original linked list is sorted
    Ex. 1 --> 2 --> 3 --> 4 --> 5  Returns 1 --> 3 --> 2 --> 5 --> 4

'''

'''                             My Solution                              '''
def linkedList_low_high(head):
    """
    Takes in a sorted linked lists and returns a low --> high ---> low form.
    :param head: The head of a linked list
    :return: The head of the new linked list that is in low/high form
    """
    current = head
    lessThan = True    #lessThan will oscillate back and forth for each node

    while current.next != None:
        lessThan = SwapHelper(current, lessThan)
        current = current.next
    return head


def SwapHelper(current, lessThan):
    """
    Helper function to swap two nodes if the data does not mach low/high form
    :param current: The current node you are looking at (access next node with current.next)
    :param lessThan: A Boolean value to signify what the correct order of low/high is for this Node.
    :return: Returns lessThan flipped from its original value for the next Node
    """
    if lessThan:
        if current.data < current.next.data:
            return False
        else:
            tmp = current.data
            current.data = current.next.data
            current.next.data = tmp
            return False
    else:
        if current.data > current.next.data:
            return True
        else:
            tmp = current.data
            current.data = current.next.data
            current.next.data = tmp
            return True

'''Notes:
    * I feel like there is probably a much cleaner way to do this with recursion or better if else composition in the helper function.
    * This is way too complex for the task it is completeing! Needs to be refactored
    * Because we have a changing state where things need to flip flop like in this problem it is useful to just use a Boolean flag.
'''

'''                             Book Solution                            '''
def alternate(ll):
    even = True
    cur = ll

    while cur.next:
        if cur.data > cur.next.data and even:
            cur.data, cur.next.data = cur.next.data, cur.data
        elif cur.data < cur.next.dat and not even:
            cur.data, cur.next.data = cur.next.data, cur.data

        even = not even
        cur = cur.next

    return ll
'''Notes:
    * Their code is a lot shorter and clearner. I do perfer explicit while statments though. Same thing happening under the hood
        but while cur.next is more confusing then while cur.next != None which is very obvious
    * I forgot swaps in Python can be completed this way!
    * Much cleaner then my implementation. I need to start refactoring my solutions before looking at the book solutions
'''

def alternate2(ll):
    prev = ll
    cur = ll.next

    while cur:
        if prev.data > cur.data:
            prev.data, cur.data = cur.data, prev.data

        if not cur.next:
            break

        if cur.next.data > cur.data:
            cur.next.data, cur.data = cur.data, cur.next.data

        prev = cur.next
        cur = cur.next.next

    return ll
'''Notes:
    * This implementation does away with using the even boolean which they think is better but I disagree. I think it is more explicit
        and says exactly what the code is doing where as this takes more mental energy to understand. This solution does not improve
        run time or space complexity and increase the difficulty of understanding the code therefore I think this is a poor solution.
'''


'''                             Test Cases                               '''
def main():
    Ex = Node(1,Node(2,Node(3,Node(4,Node(5)))))
    print(linkedList_low_high(Ex))
    help(linkedList_low_high)

if __name__ == '__main__':
    main()


'''
Lessons Learned:
    * Swaps in Python can be completed in one line, Ex: cur.data, cur.next.data = cur.next.data, cur.data
    * I need to start refactoring my solutions before looking at the book solutions
    * If a solution does not improve the algorithms run time or space complexity and adds to the overall complexity of the algorithm
        it is not a good improvement! Even if it seems fancier. Resist the urge to be fancy! Be explicit and try to make your code
        read like a sentence.
'''