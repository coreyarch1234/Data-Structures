#!python

from linkedlist import LinkedList


# implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        # TODO: Check if empty
        return self.list.is_empty() #Linked List isEmpty method

    def length(self):
        """Return the number of items in this stack"""
        # TODO: Count number of items
        if self.list.is_empty() == False:
            return self.list.length()
        else:
            return 0

    def push(self, item):
        """Insert the given item on the top of this stack"""
        # TODO: Push given item
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty"""
        # TODO: Return top item, if any
        if self.list.is_empty() == False:
            return self.list.get_at_index(0) #get first element and return it
        else:
            return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty"""
        # TODO: Remove and return top item, if any
        first_to_pop = self.list.get_at_index(0)
        self.list.delete(first_to_pop)
        return first_to_pop


# implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # Initialize a new dynamic array to store the items
        self.list = list()
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        # TODO: Check if empty
        pass

    def length(self):
        """Return the number of items in this stack"""
        # TODO: Count number of items
        pass

    def push(self, item):
        """Insert the given item on the top of this stack"""
        # TODO: Insert given item
        pass

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty"""
        # TODO: Return top item, if any
        pass

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty"""
        # TODO: Remove and return top item, if any
        pass


# implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 0:
        # s = Stack(['A', 'B', 'C'])
        s = LinkedStack(['A', 'B', 'C'])
        # print s.peek()
        # print s.length()
        print s.is_empty()
        # print s
    else:
        print('hello')


if __name__ == '__main__':
    main()
