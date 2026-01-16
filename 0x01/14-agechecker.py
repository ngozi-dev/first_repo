#!/usr/bin/python3
# a module that requests for a user age and print if they are minor or an adult

age = int(input("Enter your age: "))
if age >= 18 and age <=100:
        print("You are an adult:")
elif age <= 17 and age >=10:
        print("You are a minor: ")
else:
        print("Invalid age entered.")


        