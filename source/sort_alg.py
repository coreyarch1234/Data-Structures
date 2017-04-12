

#A way to test if a list is sorted:

def is_sorted_ascending(input_list): #assume ascending order
    # if len(input_list) <= 1:
    #     return True
    #
    # previous = input_list[0]
    # for number in input_list:
    #     if number < previous:
    #         return False
    #     previous = number
    # return True
    #
    if input_list == input_list.sort():
        return True

# Implementation of Bubble Sort method:

def bubble_sort(input_list): #worst case and average case 0(n^2)
    #condition of list being sorted
    #Loop through each pair and compare and swap if needed
    #stop loop when list sorted condition is met
    while is_sorted_ascending(input_list) is not True:
        for index in range(len(input_list) - 1):
            if input_list[index] > input_list[index + 1]:
                input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index] #swap
    return input_list

# Implementation of Selection Sort method:

def selection_sort(input_list):
    #condition of list being sorted
    #Loop through each element and hold the smallest element.
    #When you reach the end, store that least element at the start of the list
    smallest = input_list[0]
    while is_sorted_ascending(input_list) is False:
        for index in range(len(input_list)):
            if input_list[index] <= smallest:
                smallest = input_list[index]
                input_list.pop(index)
                input_list.insert(0, smallest)
    return input_list

def insertion_sort(input_list):
    #Loop through each element starting from index 1 and compare previous element with current. If previous
    # is bigger, then make current equal to that previous and make the previous index the new current index and
    #repeat until the smaller number is in the right place. O(n^2)
    for index in range(1, len(input_list)):
        current = input_list[index]
        location = index
        while location > 0 and current < input_list[location - 1]:
            input_list[location] = input_list[location - 1]
            location -= 1
        input_list[location] = current
    return input_list





def main():
    # import sys
    # args = sys.argv[1:]  # Ignore script file name
    # print(bubble_sort( [5, 1, 4, 2, 8] ))
    # print is_sorted_ascending(bubble_sort([5, 1, 4, 2, 8]))
    # print selection_sort([1,2])

    # print selection_sort([5, 1, 4, 2, 8])
    print(insertion_sort([54,26,93,17,77,31,44,55,20]))
    # print is_sorted_ascending(selection_sort([5, 1, 4, 2, 8]))


if __name__ == '__main__':
    main()
