#!/usr/bin/python3
# a module that sum the diagonal of a matrix


matrix = [[1, 2], [3, 4]]

def sum_main_diagonal(matrix):
    total = 0
    for i in range (len(matrix)):
        total += matrix[i][i]    
    return total
if __name__ == "__main__":
    result = sum_main_diagonal(matrix)
print(result)