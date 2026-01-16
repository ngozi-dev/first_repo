#!/usr/bin/python3
# a module that demonstrates conditional statements in python

age = 18
if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You are just an adult.") 
else:
    print("You are an adult.")


temperature = 10
if temperature > 30:
    print("It's a hot day. ")
elif temperature == 30: 
    print("It's a warm day. ")  
else:
    print("It's a cold day. ")


age = 22
if age < 18:
    print("You are not eligible")
else:
    print("You are eligible")
    