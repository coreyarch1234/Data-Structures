

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
                #swap instead of popping
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

def counting_sort(input_list, max_val):
    # list of 0's at indices 0...max_value
    number_counts = [0] * (max_val + 1)

    # populate num_counts
    for element in input_list:
        number_counts[element] += 1

    # populate the final sorted list
    sorted_list = []

    # for each item in num_counts
    for element, count in enumerate(number_counts):

        # for the number of times the item occurs
        for time in range(count):

            # add it to the sorted list
            sorted_list.append(element)

    return sorted_list

def mergeSort(input_list):
    if len(input_list)>1:

        mid = len(input_list)//2
        lefthalf = input_list[:mid]
        righthalf = input_list[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                input_list[k]=lefthalf[i]
                i=i+1
            else:
                input_list[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            input_list[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            input_list[k]=righthalf[j]
            j=j+1
            k=k+1

def main():
    # import sys
    # args = sys.argv[1:]  # Ignore script file name
    # print(bubble_sort( [5, 1, 4, 2, 8] ))
    # print is_sorted_ascending(bubble_sort([5, 1, 4, 2, 8]))
    # print selection_sort([1,2])

    # print selection_sort([5, 1, 4, 2, 8])
    # print(insertion_sort([54,26,93,17,77,31,44,55,20]))
    # print is_sorted_ascending(selection_sort([5, 1, 4, 2, 8]))
    # inputlist = [54,26,93,17,77,31,44,55,20]
    # mergeSort(alist)
    # print(alist)


if __name__ == '__main__':
    main()
