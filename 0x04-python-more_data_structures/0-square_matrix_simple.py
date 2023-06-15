#!/usr/bin/python3
# 0-square_matrix_simple.py


def square_matrix_simple(matrix=[]):
    """ computes the square value of all integers of a matrix."""
    result_matrix =[[0] * len(matrix[0])for_in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = matrix[i][j] ** 2

            return (result_matrix)
