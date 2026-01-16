#!/usr/bin/python3
# a module that merges two lists

num = [1, 2, 3, 4, 5]
num.extend([6, 7, 8, 9, 10])
print(num)

# 1) define the lists
list_a = [1, 3, 5]
list_b = [2, 4, 6]

# 2) merge the two lists
merged = list_a + list_b  # or: [*list_a, *list_b]

# 3) sort without using sorted()
# We'll implement a simple in-place sort (insertion sort) to keep it educational.
for i in range(1, len(merged)):
    key = merged[i]
    j = i - 1
    # Move elements of merged[0..i-1] that are greater than key to one position ahead
    while j >= 0 and merged[j] > key:
        merged[j + 1] = merged[j]
        j -= 1
    merged[j + 1] = key

# 4) print the result
print(merged)  # Expected output: [1, 2, 3, 4, 5, 6]