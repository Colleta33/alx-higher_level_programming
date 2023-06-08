#!/usr/bin/python3
if __name__ == "__main__":
''' prints the number of and the list of its arguments.'''
import sys

arguments = sys.argv[1:]  # Exclude the script name itself
num_arguments = len(arguments)

if num_arguments == 0:
    print("0 arguments.")
elif num_arguments == 1:
    print("1 argument:")
    print("1:", arguments[0])
else:
    print(num_arguments, "arguments:")
    for i, argument in enumerate(arguments, 1):
        print(i, ":", argument)
