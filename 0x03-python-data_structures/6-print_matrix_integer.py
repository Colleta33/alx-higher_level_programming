#!/usr/bin/python3
# 6-print_matrix_integer.py


def print_matrix_integer(matrix=[[]]):
    """ function that prints a matrix of integers."""
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end='')
            print()
