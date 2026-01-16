#!/usr/bin/python3
# a module that Accepts a list of integers and returns a new list containing only the even numbers.

def get_even_numbers(numbers):
    ""
    return [n for n in numbers if isinstance(n, int) and n % 2 == 0]

# Test the function with the given input
test_input = [2, 5, 8, 11, 14, 17]
result = get_even_numbers(test_input)
print(result)  # Expected output: [2, 8, 14]