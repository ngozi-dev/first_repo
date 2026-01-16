#!/usr/bin/python3
# a module that implements multiplications

def mul(a, b):
    return a * b
if __name__ =="__main__":
    num = int(input(" Enter any number of your choice: "))
    for i in range(1, 51):
        print(" {} * {} = {}" . format(num, i, mul(num, i)))
        

    