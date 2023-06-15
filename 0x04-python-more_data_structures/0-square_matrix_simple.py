#!/usr/bin/python3
# 0-square_matrix_simple.py


def square_matrix_simple(matrix=[]):
    """ computes the square value of all integers of a matrix."""
    result_matrix = list(map(lambda row: list(map(lambdax: x**2,row)), matrix))
    return (result_matrix)
