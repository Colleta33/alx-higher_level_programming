#!/usr/bin/python3
# 6-print_matrix_integer.py


def print_matrix_integer(matrix=[[]]):
    """ function that prints a matrix of integers."""
    for row in matrix
    row_str = " ".join("{:d}".format(num) for num in row)
    print(row_str)
