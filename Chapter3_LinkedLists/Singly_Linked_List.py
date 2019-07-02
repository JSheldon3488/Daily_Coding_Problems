class Node(object):
    """
    Simple Node class used as nodes for a Singly Linked List

    Attributes:
        data: can be any kind of data you wish to store in a Linked List
        next: A pointer to the next node in the Linked List
    """

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Singly_Linked_List(object):
    """
    A Singly Linked_List object is a representation of a list comprised of Node objects. Each Node has a data and a pointer to
    the next Node in the Linked List.

    Attributes:
        head: Pointer to the first Node in the Linked List
        tail: Pinter to the last Node in the Linked List
        size: An int representing how many Nodes are in the Linked List
    """

    def __init__(self, head=None):
        """
        Constructor for Singly Linked List. Can be an empty Linked List or start with a Node. Will set the size, head, and tail.

        :param head: If not set initializes to None (empty Linked List) otherwise will be the first node in the Linked List.
        """
        self.head = head
        self.tail = None
        if self.head == None:
            self.size = 0
        else:
            self.size = 1


    def __str__(self):
        """
        Printed representation of a Linked List. Printed specifically to look different than Pythons List print method.

        :return: A string representing the Linked List
        """
        s = str(self.data)
        current = self.next
        while current != None:
            s += " --> " + str(current.data)
            current = current.next
        return s


    def size(self):
        """ Returns the number of Nodes in the Linked List"""
        return self.size


    def insert(self, data):
        """
        Inserts Node to the end of the current Linked List

        :param Node: data being added to the Linked List in the form of a new Node
        """
        new_Node = Node(data)
        if self.size == 0:
            self.head = new_Node
            self.tail = new_Node
            self.size += 1
        else:
            self.tail.next = new_Node
            self.tail = new_Node
            self.size += 1


    def delete(self, data):
        """
        Deletes the Node with 'data' from the Linked List (only the first instance of 'data')

        :param data: The data that will be deleted from the Linked List
        :return: If 'data' is not present raises ValueError, if 'data' is present modifies the Linked List
        """
        # Deal with first node different then the next nodes (just move head pointer)
        current = self.head
        if current.data == data:
            self.head = current.next
            self.size -= 1
            return
        # All Nodes after first Node will move preceding .next to remove the node with the data
        while current.next != None:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return

        raise ValueError("Data not in List")


    def find(self, data):
        """
        Searches the Linked List to find 'data'. If present returns the Node, otherwise raises ValueError

        :param data: This is the data you are searching for in the Linked List
        :return: The Node where 'data' is stored, or raises exception if 'data' is not present
        """
        current = self.head
        while current != None:
            if current.data == data:
                return current
            else:
                current = current.next
        
        raise ValueError("Data not in List")
