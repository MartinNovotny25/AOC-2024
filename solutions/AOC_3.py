import numpy as np
import os 
import re

def run_solution(input_filename):
    input_path = os.path.join('inputs', input_filename)
    with open(input_path) as input_file:
        input = input_file.read()
        #print(input)

    print(f'Result for part 1: {part1(input)}')
    print(f'Result for part 2: {part2(input)}')

def part1(input):
    regex = "mul\([0-9]*,[0-9]*\)"
    matches = re.findall(regex, input)
    matches = [element.split(',') for element in matches]
    matches = [x for xs in matches for x in xs]
    matches_1 = [int(element[4:]) for ind, element in enumerate(matches) if ind % 2 == 0]
    matches_2 = [int(element[:3].replace(')', '')) for ind, element in enumerate(matches) if ind % 2 == 1]

    mul_results = sum([op1 * op2 for op1, op2 in zip(matches_1, matches_2)])
    return(mul_results)

def part2(input):
    regex_mul = "mul\([0-9]*,[0-9]*\)"
    regex_do = 'do\(\)'
    regex_dont = 'don\'t\(\)'
    joint_regex = f'({regex_mul})|({regex_do})|({regex_dont})'
    number_regex = '\d+'
    mul_enabled = True

    mul_list = []
    for match in re.finditer(joint_regex, input):
        if 'mul' in match[0]:
            if mul_enabled: 
                numbers = re.findall(number_regex, match[0])
                numbers = [int(number) for number in numbers]
                mul_list.append(numbers)
            else:
                pass    

        elif 'don\'t' in match[0]:
            mul_enabled = False
              
        elif 'do' in match[0]:
            mul_enabled = True       
                
    result = sum([number[0] * number[1] for number in mul_list])
    return result
