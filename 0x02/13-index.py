#!/usr/bin/python3
# a module that prompt user for a name and print its index if found, otherwise print "name not found."

names = ["Alice", "Bob", "Charlie", "David"]

input_name = input("Enter a name: ")

if input_name.capitalize() in names:
    index = names.index(input_name)
    print(index)
else:
    print("name not found.")
