#!/usr/bin/python3
# a module that creates a 3 x 3 matrix 

matrix = [[1,2,3], [4,5,6], [7,8,9]]
for row in matrix:
    print(row)

matrix = [1,2,3]
matrix.extend([4,5,6])
print(matrix)


matrix = [1,2,3,4,5,6]
matrix.extend([7,8,9])
print(matrix)

total = 0
for matrix in range(1, 10):  # 1 to 9 inclusive
    print(f"{total} + {matrix}")
    total += matrix
print(total)
        