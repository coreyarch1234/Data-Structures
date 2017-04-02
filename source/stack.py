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
        self.list.prepend(item) #LIFO

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
        latest = self.list.get_at_index(0)
        self.list.delete(latest)
        return latest


# implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        # Initialize a new dynamic array to store the items
        self.list = list()
        self.size = 0
        if iterable:
            for item in iterable:
                self.push(item)


    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        # TODO: Check if empty
        return self.size == 0

    def length(self):
        """Return the number of items in this stack"""
        return self.size

    def push(self, item):
        """Insert the given item on the top of this stack"""
        # TODO: Insert given item
        self.list.append(item) #LIFO
        self.size += 1

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty"""
        # TODO: Return top item, if any
        if self.is_empty():
            return None
        else:
            return self.list[self.size - 1]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty"""
        # TODO: Remove and return top item, if any
        if self.is_empty():
            raise ValueError('List does not contain any elements')
        else:
            latest = self.list[self.size - 1]
            self.list.remove(latest)
            self.size -= 1
            return latest


# implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 0:
        s = Stack()
        # s = Stack(['A', 'B', 'C'])
        # s = LinkedStack(['A', 'B', 'C'])
        # print s.peek()
        # print s.length()
        print s.is_empty()
        # print s
    else:
        print('hello')


if __name__ == '__main__':
    main()
