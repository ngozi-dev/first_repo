#!/usr/bin/python3
# a module that finds the location of a element in the matrix

matrix = [[1, 2], [3, 4]]

def find_element(matrix):
    for i in range (1, 4):
        if i % 2 == 0:
        index = matrix.index(i)
        print(index)
