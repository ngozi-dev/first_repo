#!/usr/bin/python3
# a module that Remove duplicates from a list without using set(), Preserves the original order of first occurrence.

def remove_duplicate(lst):
        cleaned = []
for item in lst:
        if item not in cleaned:
            cleaned.append(item)
        return cleaned

# Example with duplicates
original = [1, 2, 2, 3, 4, 4, 5]
cleaned = remove_duplicate(original)

print("Original list:", original)
print("Cleaned list :", cleaned)