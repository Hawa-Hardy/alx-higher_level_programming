#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_mat = []
    for line in matrix:
        squared_mat.append([c**2 for c in line])
    return squared_mat
