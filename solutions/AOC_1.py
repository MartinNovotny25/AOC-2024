import numpy as np
import os
var = 0

def run_solution(input_file_name):

    input_path = os.path.join('inputs', input_file_name)
    arr_left    = []
    arr_right   = []

    with open(input_path) as input_file:
        for line in input_file:
            split_line = line.split(' ')
            split_line.remove(''), split_line.remove('')
            split_line[-1] = split_line[-1].replace('\n', '')
            arr_left.append(split_line[0])
            arr_right.append(split_line[-1])
            
    pivot_index         = 0
    sorted_arr_left     = my_sort(arr_left, 0, len(arr_left), pivot_index)
    sorted_arr_right    = my_sort(arr_right, 0, len(arr_right), pivot_index)

    print(f"Result for part 1: {part1(sorted_arr_left, sorted_arr_right)}")
    print(f"Result for part 2: {part2(sorted_arr_left, sorted_arr_right)}")

def part1(sorted_arr_left, sorted_arr_right):
    acc = 0
    for left, right in zip(sorted_arr_left, sorted_arr_right):
        distance = np.abs(int(left) - int(right))
        acc += distance
    return acc 

def part2(sorted_arr_left, sorted_arr_right):
    right_occurences = {}
    acc = 0

    for item in sorted_arr_right:
        if item not in right_occurences.keys():
            right_occurences[item] = 1
        else:
            right_occurences[item] += 1

    for item in sorted_arr_left:
        if item in right_occurences.keys():
            acc += int(item) * int(right_occurences[item])
    return acc        



def my_sort(unsorted_list, left, right, pivot_index):

    if len(unsorted_list[left:right]) == 0:
        return unsorted_list
    
    if len(unsorted_list[left:right]) == 1:
        return unsorted_list
    
    elif len(unsorted_list[left:right]) == 2:
        if unsorted_list[left] > unsorted_list[left+1]:
            unsorted_list[left], unsorted_list[left+1] = unsorted_list[left+1], unsorted_list[left]
            return unsorted_list
        else:
            return unsorted_list
    
    j = left
    pivot = unsorted_list[pivot_index]

    # Swap pivot with last index
    unsorted_list[right-1], unsorted_list[pivot_index] = unsorted_list[pivot_index], unsorted_list[right-1]

    for i in range(left,right-1):
        if unsorted_list[i] < pivot:
            unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
            j += 1

    unsorted_list[right-1], unsorted_list[j] = unsorted_list[j], unsorted_list[right-1]

    unsorted_list = my_sort(unsorted_list, left, j, left)
    unsorted_list = my_sort(unsorted_list, j+1, right, j+1)      
    return unsorted_list

    



        




      






