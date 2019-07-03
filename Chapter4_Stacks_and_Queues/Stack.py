class Stack:
    """
    A basic Stack class following "last in, first out" principle. Supports methods push, pop, peek, and size. The stack is
    initialized as empty.

    Attributes:
        Size: Keeps track of the size of the stack
    """
    def __init__(self):
        """
        Initializes the stack to an empty list with size 0
        """
        self.stack = []
        self.size = 0

    def __str__(self):
        """ Returns String representation of the stack. Top of stack is first element printed"""
        s = "Stack( "
        for i in range(self.size -1, -1, -1):
            s += str(self.stack[i])
            if i != 0:
                s += " --> "
        s += " )"
        return s

    def push(self,data):
        """
        Pushes 'data' onto the top of the stack (the back of the list)
        :param data: data to be pushed onto the stack
        """
        self.stack.append(data)
        self.size += 1

    def pop(self):
        """
        Returns and removes the 'data' from the top of the stack
        :return: data from the top of the stack
        """
        if self.size == 0:
            raise ValueError("The Stack is Empty")
        self.size -= 1
        return self.stack.pop()

    def peek(self):
        """
        Returns the 'data' from the top of the stack but does not remove the data.
        :return: 'data from the top of the stack
        """
        if self.size == 0:
            raise ValueError("The Stack is Empty")
        return self.stack[-1]