"""
Date: 7/3/19
4.1: Implement a Max Stack
"""

'''
Problem Statement: Implement a stack that has the following methods
    push(val): pushs val onto the stack
    pop: pop off and return the topmost element of the stack. If there are no elements in the stack, throw an error.
    max: Return the max value in the stack currently. If there are no elements in the stack, throw an error.

'''


'''                             My Solution                              '''
class MaxStack:
    """
    A modified Stack class following "last in, first out" principle. Supports methods push, pop, and max. The stack is
    initialized as empty.

    Attributes:
        Size: Keeps track of the size of the stack
        Max: Max value seen so far in the stack
    """

    def __init__(self):
        """
        Initializes the stack to an empty list with size 0
        """
        self.stack = []
        self.size = 0
        self.max_seen = float('-inf')
        self.prev_max = float('-inf')

    def __str__(self):
        """ Returns String representation of the stack. Top of stack is first element printed"""
        s = "Stack( "
        for i in range(self.size - 1, -1, -1):
            s += str(self.stack[i])
            if i != 0:
                s += " --> "
        s += " )"
        return s

    def push(self, data):
        """
        Pushes 'data' onto the top of the stack (the back of the list)
        :param data: data to be pushed onto the stack
        """
        self.stack.append(data)
        self.size += 1
        if data > self.max_seen:
            self.prev_max = self.max_seen
            self.max_seen = data

    def pop(self):
        """
        Returns and removes the 'data' from the top of the stack
        :return: data from the top of the stack
        """
        if self.size == 0:
            raise ValueError("The Stack is Empty")
        self.size -= 1
        res = self.stack.pop()
        if res == self.max_seen:
            self.max_seen = self.prev_max
        return res

    def max(self):
        """ Returns the max value in the current stack """
        return self.max_seen

'''Notes:
    * Will not quite work because we can only backtrack 1 item. Need a way to backtrack more items.
    * Solution Below in Books solution
'''


'''                             Book Solution                            '''
class MaxStack_Book:
    """
    This is the book solution of MaxStack slightly modified for printing and stuff
    """

    def __init__(self):
        """
        Initializes the stack to an empty list with size 0, uses a max stack to keep track of max seen at each push
        """
        self.stack = []
        self.maxes = []

    def __str__(self):
        """ Returns String representation of the stack. Top of stack is first element printed"""
        s = "Stack( "
        for i in range(len(self.stack) - 1, -1, -1):
            s += str(self.stack[i])
            if i != 0:
                s += " --> "
        s += " )"
        return s

    def push(self, data):
        """
        Pushes 'data' onto the top of the stack (the back of the list) and updates the maxes stack accordingly
        :param data: data to be pushed onto the stack
        """
        self.stack.append(data)
        if self.maxes:
            self.maxes.append(max(data, self.maxes[-1]))
        else:
            self.maxes.append(data)

    def pop(self):
        """
        Returns and removes the 'data' from the top of the stack, also updates maxes accordingly
        :return: data from the top of the stack
        """
        if self.maxes:
            self.maxes.pop()
        return self.stack.pop()

    def max(self):
        """ Returns the max value in the current stack """
        return self.maxes[-1]

'''Notes:
    * I like their use of max() to compare between two items instead of having to use a conditional and branching for that
    * Their if, else to deal with the list initially being empty is handy
    * This is a much clearner, more elegent solution than I came up with.
'''


'''                             Test Cases                               '''
def main():
    print("My Soltion")
    s = MaxStack()
    s.push(9), s.push(2), s.push(10), s.push(30)
    print(s)
    print(s.max())
    s.pop()
    print(s)
    print(s.max())
    s.pop()
    print(s)
    print(s.max())
    s.pop()
    print(s)
    print(s.max())
    print("Trouble backtracking more then one previous max element")

    print()
    print("Book Solution")
    b = MaxStack_Book()
    b.push(9), b.push(2), b.push(10), b.push(30)
    print(b)
    print(b.max())
    b.pop()
    print(b)
    print(b.max())
    b.pop()
    print(b)
    print(b.max())
    b.pop()
    print(b)
    print(b.max())


if __name__ == '__main__':
    main()


'''
Lessons Learned:
    * Stacks can be used to be able to backtrack more then one item! This is a great example of how to back track multiple max's
        by knowing what the max was at that exact push.
    * Really understanding your data structures so that you know how to use them to solve unique problems is and important skill to master.
    * When you think of min_seen, or max_seen consider using a stack, especially if you have to backtrack!
    * If you are using already built in data structures you can use their attributes and methods to solve your problems for this data structure.
'''
