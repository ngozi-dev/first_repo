#!/usr/bin/python3
# a module that creates different types of variables

name = "Emeka Ezeaku" # string variable
age = 25 # integer variable
height = 5.9 # float variable
Nigerian = True # boolean variable
first = "Ngozi"
last_name = "Okafor"
course = 'Python "Programming'
print(course)
course = "Python \"Programming"
print(course)
course = "Python Programming"
print(course[0:]) # prints the entire string
print(course[:]) # prints the entire string
print(course[0:3]) # prints characters from index 0 to 2
print(course[0]) # prints character at index 0
print(course[7]) # prints character at index 7
print(course[-1]) # prints the last character
print(course[0:6]) # prints characters from index 0 to 5
print(len(course)) # prints the length of the string stored in course variable
print("My name is " + first + " " + last_name)   
print( "Hello " + name)
print(age)
print(height)  
print(Nigerian) 

print(course.upper()) # prints the string in uppercase
print(course.lower()) # prints the string in lowercase
print(course.title()) # prints the string in title case
print(course.replace("Programming", "Development")) # replaces "Programming" with "Development"
print(course.split()) # splits the string into a list of words
print("Programming" in course) # checks if "Programming" is in the string
print(course.strip()) # removes any leading/trailing whitespace
print(course.find("Python")) # finds the index of the substring "Python"
print(course.count("o")) # counts the occurrences of the letter "o" 