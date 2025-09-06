import os

def run_solution(input_filename):
    input_path = os.path.join('inputs', input_filename)
    with open(input_path) as input_file:
        input = input_file.read()

        print(f"Result for part 1: {part1(input)}")

def part1(input : str):

    line_list = input.split('\n')
    line_length = len(line_list[0])
    number_of_lines = len(line_list)
    counter = 0
    for line_index, line in enumerate(line_list):
        for char_index, char in enumerate(line):
            # Left direction
            if char_index >= 3:
                if line[char_index-3:char_index+1] == "SAMX":
                    counter += 1
            # Right 
            if char_index <= line_length-4:
                if line[char_index:char_index+4] == "XMAS":
                    counter += 1 
            # Down
            if line_index <= number_of_lines-5:
                line_slice = line_list[line_index:line_index+4]
                vertical_chars = ''.join([line[char_index] for line in line_slice])
                if vertical_chars == "XMAS":
                    counter +=1
            # Up
            if line_index >= 3:
                line_slice = line_list[line_index-3:line_index+1]
                vertical_chars = ''.join([line[char_index] for line in line_slice])
                if vertical_chars == "SMAX":
                    counter +=1

            # Diagonal left
            if         

        #break            



    print(counter)                
