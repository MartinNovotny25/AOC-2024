# Martin Novotný Mlinárcsik
# AoC day 2

# Primarily, I wanted to work with Python slicing and list comprehension as much as possible.

# Part 1
# After processing the input, we determine of each record is both safe in terms of distances and increasing/decreasing
# For each record, create a new array that will contain succesive pairs of levels. For each level, check if
# they are ascending or descending, and if they are within safe distance. If the record is safe, return True, else False.
# The result of is_descending and is_ascending is a Boolean array, which serves as a mask to filter out Unsafe records.
# Unsafe records are filtered out, and the resultant amount of remaining records are all safe records.

# Part 2
# Because we determine what pairs are Unsafe, we can either remove the first or the second to see if it fixes the problem
# Left/Right element is removed, and Safety calculation is done again on filtered list.

import numpy as np
import os
from functools import reduce

def run_solution(input_filename):
    input_path = os.path.join('inputs', input_filename)
    with open(input_path) as input_file:
        input = input_file.read()
        input = input.split('\n')
        input = [report.split(' ') for report in input]
        input.pop(-1)
        
        # Find longest report
        largest_length = 0
        for report in input:
            if len(report) > largest_length:
                largest_length = len(report)
            else:
                continue    
        
        # Fill dummy values to reports whose lengths are smaller that largest_length
        # so np.array can be used
        filled_reports = [element + ['-1']*(largest_length-len(element)) for element in input]
        report_array = np.array(filled_reports).astype(np.integer)

        print(f'Result for part 1: {part1(report_array)}')
        print(f'Result for part 1: {part2(report_array)}')

def part1(report_array : np.ndarray[np.integer] ):

    # First masks
    safe_decreasing_mask = np.array(list(map(is_decreasing, report_array, np.zeros_like(report_array))))
    safe_increasing_mask = np.array(list(map(is_increasing, report_array, np.zeros_like(report_array))))

    # Filter out safe decreasing and increasing reports
    safe_decreasing_reports = report_array[safe_decreasing_mask]
    safe_increasing_reports = report_array[safe_increasing_mask]

    return(safe_decreasing_reports.shape[0] + safe_increasing_reports.shape[0])

def part2(report_array : np.ndarray[np.integer]):

     # First masks
    safe_decreasing_mask = np.array(list(map(is_decreasing, report_array, np.ones_like(report_array))))
    safe_increasing_mask = np.array(list(map(is_increasing, report_array, np.ones_like(report_array))))


    # Filter out safe decreasing and increasing reports
    safe_decreasing_reports = report_array[safe_decreasing_mask]
    safe_increasing_reports = report_array[safe_increasing_mask]

    return(safe_decreasing_reports.shape[0] + safe_increasing_reports.shape[0])
    


def is_decreasing(report, part):

        # Filter out dummy '-1' values used to create the original np_array
        filtered_report = report[report != -1]

        # Create lists each 2 succesive pairs
        succesive_pairs = [[filtered_report[i-1], filtered_report[i]] for i in range(1, len(filtered_report))]

        # Boolean value if the first value is larger than the second -> decreasing pair
        all_decreasing = np.array([val[0] > val[1] and np.abs(val[0] - val[1]) <= 3 for val in succesive_pairs])

                                  
         # Once we have bool array, check if changing 1 level can make the record safe
        if part[0] == 1:

            # Get indexes of False IDs
            false_ids = np.where(all_decreasing == False)[0]

            # If only 1 unsafe level pair is detected, there are 2 options
            # Delete left or right, either can possibly fix the safety
            if len(false_ids) == 1: 
                del_l_all_decreasing = False
                del_r_all_decreasing = False
                if false_ids[0] >= 0:
                    deleted_left_report = np.delete(filtered_report, false_ids[0])
                    del_l_succesive_pairs = [[deleted_left_report[i-1], deleted_left_report[i]] for i in range(1, len(deleted_left_report))]
                    del_l_all_decreasing =  np.array([val[0] > val[1] and np.abs(val[0] - val[1]) <= 3 for val in del_l_succesive_pairs])
                    del_l_all_decreasing = all(del_l_all_decreasing)

                if del_l_all_decreasing == False:
                    deleted_right_report = np.delete(filtered_report, false_ids[0]+1)
                    del_r_succesive_pairs = [[deleted_right_report[i-1], deleted_right_report[i]] for i in range(1, len(deleted_right_report))]
                    del_r_all_decreasing =  np.array([val[0] > val[1] and np.abs(val[0] - val[1]) <= 3 for val in del_r_succesive_pairs])
                    del_r_all_decreasing = all(del_r_all_decreasing)

                return del_l_all_decreasing | del_r_all_decreasing     
                    
            # If there are 2 unsafe pairs, they must be 2 successive pairs in order for fix to be possibile
            # Check if removing the middle level can make safe record
            elif len(false_ids) == 2 and false_ids[0] == false_ids[1] -1:                
                # Delete the middle level
                filtered_report = np.delete(filtered_report, false_ids[1])
                succesive_pairs = [[filtered_report[i-1], filtered_report[i]] for i in range(1, len(filtered_report))]
                all_decreasing = all_decreasing = np.array([val[0] > val[1] and np.abs(val[0] - val[1]) <= 3 for val in succesive_pairs])
                all_decreasing = all(all_decreasing)
                return all_decreasing


            # If there are more than 2 unsafe levels, pass
            else:
                all_decreasing  = all(all_decreasing)
                return all_decreasing          
        else:         

            all_decreasing  = all(all_decreasing)
            return all_decreasing

def is_increasing(report, part):

        # Filter out dummy '-1' values used to create the original np_array
        filtered_report = report[report != -1]

        # Create lists each 2 succesive pairs
        succesive_pairs = [[filtered_report[i-1], filtered_report[i]] for i in range(1, len(filtered_report))]
        # Boolean value if the first value is larger than the second -> decreasing pair
        all_increasing = np.array([val[0] < val[1] and np.abs(val[0] - val[1]) <= 3 for val in succesive_pairs])

        # Once we have bool array, check if changing 1 level can make the record safe
        if part[0] == 1:

            # Get indexes of False IDs
            false_ids = np.where(all_increasing == False)[0]

            # If only 1 unsafe level pair is detected, there are 2 options
            # Delete left or right, either can possibly fix the safety
            if len(false_ids) == 1: 
                del_l_all_increasing = False
                del_r_all_increasing = False
                if false_ids[0] >= 0:
                    deleted_left_report = np.delete(filtered_report, false_ids[0])
                    del_l_succesive_pairs = [[deleted_left_report[i-1], deleted_left_report[i]] for i in range(1, len(deleted_left_report))]
                    del_l_all_increasing =  np.array([val[0] < val[1] and np.abs(val[0] - val[1]) <= 3 for val in del_l_succesive_pairs])
                    del_l_all_increasing = all(del_l_all_increasing)

                if del_l_all_increasing is not True:
                    deleted_right_report = np.delete(filtered_report, false_ids[0]+1)
                    del_r_succesive_pairs = [[deleted_right_report[i-1], deleted_right_report[i]] for i in range(1, len(deleted_right_report))]
                    del_r_all_increasing =  np.array([val[0] < val[1] and np.abs(val[0] - val[1]) <= 3 for val in del_r_succesive_pairs])
                    del_r_all_increasing = all(del_r_all_increasing)

                return del_l_all_increasing | del_r_all_increasing     
                    
            # If there are 2 unsafe pairs, they must be 2 successive pairs in order for fix to be possibile
            # Check if removing the middle level can make safe record
            elif len(false_ids) == 2 and false_ids[0] == false_ids[1] -1:                
                # Delete the middle level
                filtered_report = np.delete(filtered_report, false_ids[1])
                succesive_pairs = [[filtered_report[i-1], filtered_report[i]] for i in range(1, len(filtered_report))]
                all_increasing = all_increasing = np.array([val[0] < val[1] and np.abs(val[0] - val[1]) <= 3 for val in succesive_pairs])
                all_increasing = all(all_increasing)
                return all_increasing


            # If there are more than 2 unsafe levels, pass
            else:
                all_increasing  = all(all_increasing)
                return all_increasing          
        else:         

            all_increasing  = all(all_increasing)
            return all_increasing

