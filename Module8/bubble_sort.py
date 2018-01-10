#!/usr/bin/python3
# This program sorts using the Bubble Sort algorithm.
# The bubble sort passes through a list of values from start to finish comparing 
# each sequential pair of values. If the values compared are not in order, 
# they are swapped. The sort begins at the start of the list, first comparing 
# the values in position 0 and 1, next the values in positions 1 and 2, 
# then those in positions 2 and 3, and so on until the end of the list is reached. 
# If the entire list is not in the correct order when the sort reaches 
# the end of the list, the sort will start at the beginning of the list and 
# pass through it again. The sort will continue its passes through the list 
# until the list is sorted.

int_str = input("Please input a list of comma-separated integers (ex. 9,5,6,2,66,33,1): ")
int_list = int_str.split(",")

# function to turn a list or tuple of integers into a string
# formatted with commas between each number
def list_tup_to_str(list_or_tup):
    final_str = ""
    for i, num in enumerate(list_or_tup):
        if i == len(list_or_tup) - 1:
            final_str += str(num)
        else:
            final_str += str(num) + ","
    return final_str

def bubble_sort(lst):
    passes = 0
    n = len(lst)

    # keep running while loop until no values swap places after a complete pass
    while True:
        swapped = False
        for i in range(1, n):
            if lst[i - 1] > lst[i]:
                lst[i - 1], lst[i] = lst[i], lst[i - 1]
                # set to True if a change was made to the list
                swapped = True
        passes += 1
        # decrements n by 1 because bubble sort pushes the bigger number to 
        # the top, so after the first pass, largest number should be at the top
        # do not need to re-sort the already sorted numbers at the top
        n -= 1
        partial_sorted = list_tup_to_str(lst)
        print("Pass " + str(passes) + ": " + partial_sorted)
        # if no values swapped places after a complete pass, break out of loop
        if not swapped:
            break
    return lst, passes

sorted_list, passes = bubble_sort(int_list)
print("Original List: " + int_str)
sorted_int_str = list_tup_to_str(sorted_list)
print("Sorted List: " + sorted_int_str)
print("Number of Passes: " + str(passes))