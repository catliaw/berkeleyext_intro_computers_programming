#!/usr/bin/python3
# This program consists of a user-defined function called sort_and_mean
# which takes a list of numbers as an argument and sorts and PRINTS that 
# list of numbers. The function also calculates and RETURNS the mean value
# numberse in the list.
# Test input: [3,9,7,4,0,2]

def sort_and_mean(nums_list):
    sorted_list = []
    total = None
    list_length = len(nums_list)

    while nums_list:
        minimum = nums_list[0]
        for num in nums_list:
            if num < minimum:
                minimum = num
        sorted_list.append(minimum)
        nums_list.remove(minimum)
        if total is None:
            total = minimum
        else:
            total += minimum

    average = float(total) / float(list_length)

    print("Sorted list of numbers:")
    print(sorted_list)
    print("\nAverage of numbers:")
    print(average)
    return average

sort_and_mean([3,9,7,4,0,2])
