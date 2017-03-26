#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests below
    # array.sort()
    print(array)
    if index == len(array):
        return None
    if item == array[index]:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left = 0 #Start of list
    right = len(array) - 1 #End of list
    item_found = False
    while item_found is not True:
        diff = right - left
        if diff <= 1: #Meaning the right and left are consecutive, in which case there are no more cases to check
            if array[right] == item: #The item must be either at the right or left unless it does not exist.
                return right
            elif array[left] == item:
                return left
            else:  # if array[right] != item and array[left] != item:
                return None
        middle = (left + right) / 2
        if array[middle] == item:
            item_found = True
        elif item > array[middle]:
            # left += half
            left = middle
        elif item < array[middle]:
            # right -= half
            right = middle
    return middle


def binary_search_recursive(array, item, left=None, right=None):
    if left == None: #Will only happen once
        left = 0 #Start of list
        right = len(array) - 1 #End of list
    # assert len(array) >= 1
    # if item == array[0]: #If the item is at the start
    #     return 0
    # if item == array[len(array) - 1]: #If the item is at the ends
    #     return len(array) - 1
    diff = right - left
    if diff <= 1: #Meaning the right and left are consecutive, in which case there are no more cases to check
        # print(left)
        # print(right)
        # print(array[left])
        # print(item)
        if array[right] == item: #The item must be either at the right or left unless it does not exist.
            return right
        elif array[left] == item:
            return left
        else:  # if array[right] != item and array[left] != item:
            return None
    # half = diff/2
    # middle = left + half
    middle = (left + right) / 2
    if array[middle] == item:
        return middle
    elif item > array[middle]:
        # left += half
        left = middle

        #Maybe add a current index to add to half
        return binary_search_recursive(array, item, left, right)
    elif item < array[middle]:
        # right -= half
        right = middle
        #Maybe add a current index to add to half
        return binary_search_recursive(array, item, left, right)



def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 8:
        # element_1 = args[0]
        # element_2 = args[1]
        # element_3 = args[2]
        # element_4 = args[3]
        # element_5 = args[4]
        # element_6 = args[5]
        # element_7 = args[6]
        # array = list([element_1, element_2, element_3, element_4, element_5, element_6, element_7])
        # item = args[7]
        # result = linear_search_iterative(array, item)
        # result = binary_search(array, item)
        # binary_search(array, item)
        element_1 = args[0]
        element_2 = args[1]
        element_3 = args[2]
        element_4 = args[3]
        element_5 = args[4]
        element_6 = args[5]
        element_7 = args[6]
        item = args[7]
        array = [element_1, element_2, element_3, element_4, element_5, element_6, element_7]
        # result = linear_search_recursive(array, item)
        # linear_search_recursive(array, item)
        result = binary_search(array, item)
        print(result)
        # print('factorial({}) => {}'.format(num, result))
    else:
        print('Usage: {} number'.format(sys.argv[0]))
if __name__ == '__main__':
    main()
