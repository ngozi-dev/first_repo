#!/usr/bin/python3
# a module that displays password

password = "ngozi123"
user_input = input("Enter your password: ")
while user_input != password:
    print("Incorrect password. Try again. ")
    user_input = input("Enter your password: ")

if user_input == password:
        print("Access granted. welcome!")
    
