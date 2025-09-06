# Author: Martin Novotný Mlinárcsik
# Advent of code 2025
# main.py is used to run all solutions for the Advent of Code 2025

import argparse

def main():
    arg_parser = argparse.ArgumentParser(
                    prog="main.py",
                    description="Run Advent of Code 2025 solutions by specifying day number as an argument")
    
    arg_parser.add_argument('-d', '--day', required=True, type=int ,help='Which day you want to run')
    arg_parser.add_argument('-i', '--input', required=True, type=str, help='Input file for given day')

    args = arg_parser.parse_args()

    match args.day:
        case 1:  
            import solutions.AOC_1
            solutions.AOC_1.run_solution(args.input)
        case 2:  
            import solutions.AOC_2
            solutions.AOC_2.run_solution(args.input)
        case 3:  
            import solutions.AOC_3
            solutions.AOC_3.run_solution(args.input)
        case 4:  
            import solutions.AOC_4
            solutions.AOC_4.run_solution(args.input)                  
        case 5:  
            import solutions.AOC_3
            solutions.AOC_3.run_solution(args.input)  
        case 6:  
            import solutions.AOC_3
            solutions.AOC_3.run_solution(args.input)              
        case 7:  
            import solutions.AOC_3
            solutions.AOC_3.run_solution(args.input)  



if __name__ == "__main__":
    main()
    