
from queue import LinkedQueue

class BinaryNode(object):

    def __init__(self, data):
        """Initialize this binary node with the given data"""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary node"""
        return 'BinaryNode({})'.format(repr(self.data))

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)"""
        # TODO: Check if both left child and right child have no value
        return self.left is None and self.right is None #true if there is no left and right child

    def is_internal(self):
        """Return True if this node is internal (has at least one child)"""
        # TODO: Check if either left child or right child has a value
        return self.left is not None or self.right is not None

    def height(self):
        """Return the number of edges on the longest downward path from this
        node to a descendant leaf node"""
        if self.left is not None:
            left_height = self.left.height() + 1
        else:
            left_height = -1

        if self.right is not None:
            right_height = self.right.height() + 1
        else:
            right_height = -1

        return 1 + max(left_height, right_height)


        # # TODO: Check if left child has a value and if so calculate its height
        # left_height = ... if self.left is not None else -1
        # # TODO: Check if right child has a value and if so calculate its height
        # right_height = ... if self.right is not None else -1
        # # Return one more than the greater of the left height and right height
        # return 1 + max(left_height, right_height)


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items"""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree"""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree contains no nodes"""
        return self.root is None

    def height(self):
        """Return the number of edges on the longest downward path from this
        tree's root node to a descendant leaf node (the height of the root)"""
        # Check if root node has a value and if so calculate its height
        return self.root.height() if self.root is not None else -1

    def contains(self, item):
        """Return True if this binary search tree contains the given item"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # TODO: Return the node's data if found, or None
        return node.data if node is not None else None

    def _find_node(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            # TODO: Check if the given item is less than the node's data
            elif item < node.data:
                    # TODO: Descend to the node's left child
                    node = node.left
                # TODO: Check if the given item is greater than the node's data
            elif item > node.data:
                    # TODO: Descend to the node's right child
                    node = node.right
        # Not found
        return None

    def _find_parent_node(self, item):
        """Return the parent node of where the given item is (or would be) in
        this binary search tree, or None if this tree has only a root node"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node, which is None
                return parent
            # TODO: Check if the given item is less than the node's data
            elif item < node.data:
                    # TODO: Update the parent and descend to the node's left child
                    parent = node
                    node = node.left
                # TODO: Check if the given item is greater than the node's data
            elif item > node.data:
                    # TODO: Update the parent and descend to the node's right child
                    parent = node
                    node = node.right
        # Not found
        return parent

    def insert(self, item):
        """Insert the given item in order into this binary search tree"""
        # Handle the case where the tree is empty
        if self.is_empty():
        # if self.root is None:
            # TODO: Create a new root node
            self.root = BinaryNode(item)
            # TODO: Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node(item)
        # print('hello')
        print(parent)
        # TODO: Check if the given item should be inserted left of the parent node
        if item < parent.data:
            # TODO: Create a new node and set the parent's left child
            parent.left = BinaryNode(item)
        # TODO: Check if the given item should be inserted right of the parent node
        elif item > parent.data:
                # TODO: Create a new node and set the parent's right child
                parent.right = BinaryNode(item)
            # TODO: Increase the tree size
        self.size += 1





    def items_in_order(self, node=None, items=None):
        """Return a list of all items in this binary search tree found using
        in-order traversal starting at the given node after the given items"""
        # Set up starting node and items list if not given
        if items is None and node is None:
            items = list()
            node = self.root
        if node is not None: #if the node is empty, return
            self.items_in_order(node.left, items) #check the left of the node and if it does not exist, move on to append and check right.
            items.append(node.data) #'visit'
            self.items_in_order(node.right, items) #check right and if it doesn not exist, return with visit
        # Return the items list to the original caller
        return items

    def sort_items_in_order(self):
        sorted_list = self.items_in_order()
        return sorted_list


    def items_pre_order(self, node=True, items=None):
        """Return a list of all items in this binary search tree found using
        pre-order traversal starting at the given node after the given items"""
        # Set up starting node and items list if not given
        if node is True:
            node = self.root
        if items is None:
            items = list()

        if node is not None:
            items.append(node.data)
            self.items_pre_order(node.left, items)
            self.items_pre_order(node.right, items)
        return items


    def items_post_order(self, node=True, items=None):
        """Return a list of all items in this binary search tree found using
        post-order traversal starting at the given node after the given items"""
        # Set up starting node and items list if not given
        if node is True:
            node = self.root
        if items is None:
            items = list()

        if node is not None:
            self.items_post_order(node.left, items)
            self.items_post_order(node.right, items)
            items.append(node.data)
        return items

    def items_level_order(self):
        """Return a list of all items in this binary search tree found using
        level-order traversal"""
        queue = LinkedQueue()
        # Create an items list
        items = list()
        if self.is_empty() is False:
            queue.enqueue(self.root)
        while queue.is_empty() is False:
            node = queue.dequeue()
            items.append(node.data)
            if node.left is not None:
                queue.enqueue(node.left)
            if node.right is not None:
                queue.enqueue(node.right)
        # Return the items list
        return items



    # def delete(self, item):
    #     """Delete the given item in this binary search tree"""
    #     node = self._find_node(item)
    #     node_parent = self._find_parent_node(item)
    #     count_children = 0
    #     if node is not None:
    #         if node.left is not None:
    #             count_children += 1
    #         if node.right is not None:
    #             count_children += 1
    #     #case 1 is where the node has no count_children. Look for node and set it's parent's left or right child to None
    #     if count_children == 0:
    #         if node_parent.left is node: #If the parent's left child is the node to be deleted.
    #             node_parent.left = None
    #             self.size -= 1
    #         if node_parent.right is node: #If the parent's right child is the node to be deleted.
    #             node_parent.right = None
    #             self.size -= 1
    #         if node_parent is self.root:
    #             self.root = None
    #             self.size -= 1
    #     # if the parent is the root node, clear its data
    #
    #
    #     #case where the node has 1 children. Make parent's left or right child equal to the node's left or right child. Basically, replace node with its child.
    #     if count_children == 1:
    #         if node.left is not None:
    #             replacement_node = node.left
    #         elif node.right is not None:
    #             replacement_node = node.right
    #         if node_parent.left == node:
    #             node_parent.left = replacement_node
    #         elif node_parent.right == node:
    #             node_parent.right = replacement_node
    #         self.size -= 1
    #         # del node
    #         if node == self.root:
    #             node = replacement_node
    #             self.size -= 1
    #     #case where the node has 2 children. Locate the node and find it's rightmost descendent in the left subtree relative to it. Then replace the node
    #     #with that rightmost node and
    #     if count_children == 2:
    #         if node.left is not None:
    #             replacement_node = node.left
    #             while replacement_node.right is not None: #get the rightmost node on the left subtree of the node to be deleted
    #                 replacement_node = replacement_node.right
    #             if node_parent.left == node:
    #                 node_parent.left = replacement_node
    #             elif node_parent.right == node:
    #                 node_parent.right = replacement_node
    #             del replacement_node
    #             self.size -= 1
    #         elif node.left is None:
    #             replacement_node = node.right
    #             while replacement_node is not None:
    #                 replacement_node = replacement_node.left
    #             if node_parent.left == node:
    #                 node_parent.left = replacement_node
    #             elif node_parent.right == node:
    #                 node_parent.right = replacement_node
    #             del replacement_node
    #             self.size -= 1



def test_binary_search_tree():

    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    # print('items: ' + str(items))
    #
    bst = BinarySearchTree([54,26,93,17,77,31,44,55,20])
    print(bst.sort_items_in_order())
    # items = [4, 2, 6, 1, 3, 5, 7]
    # print(bst.sort_items_in_order(items))
    # print('tree: ' + str(bst))
    # print('root: ' + str(bst.root))
    #
    # print('\nInserting items:')
    # for item in items:
    #     bst.insert(item)
    #     # print('insert({})'.format(item))
    #     print('insert({}), size: {}'.format(item, bst.size))
    #     # print(bst)
    # print('root: ' + str(bst.root))
    #
    # print('\nSearching for items:')
    # for item in items:
    #     result = bst.search(item)
    #     print('search({}): {}'.format(item, result))
    # item = 123
    # result = bst.search(item)
    # print('search({}): {}'.format(item, result))
    # print(bst)
    #
    # print('\nTraversing items:')
    # print('items in-order:    ' + str(bst.items_in_order()))
    # print('items pre-order:   ' + str(bst.items_pre_order()))
    # print('items post-order:  ' + str(bst.items_post_order()))
    # print('items level-order: ' + str(bst.items_level_order()))

if __name__ == '__main__':
    test_binary_search_tree()
