#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        squared_row = [element ** 2 for element in row]
        result.append(squared_row)
    return result
