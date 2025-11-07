#!/usr/bin//python3
# a module that displays user grades

score = int(input("Enter any number of your choice: "))
if score >= 90 and score <= 100:
        print("You have A grade")
elif score <= 69 and score >=60:
        print("You have B grade")
elif score >=50 and score <=49:
        print("You have C grade")
elif score >=40 and score <=39:
        print("You have D grade")
else:
        print("IYou have F grade")




