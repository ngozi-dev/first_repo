#!/usr/bin/python3
# a module that demonstrates logical operators in python

# we have three logical operators in python: and, or, not

# Example using 'and' operator
age = 25
income = 50000  
if age > 18 and income > 30000:
    print("You are eligible for the loan. ")
else:
    print("You are not eligible for the loan. ")

# Example using 'or' operator
temperature = 35
if temperature > 30 or temperature < 10:
    print("Extreme weather conditions. ")   
else:
    print("Moderate weather conditions. ")
    