#Variables and Data

a = "Hello, World"
print(a)


Age = int(input("Enter Your Age: "))
print("I'm", Age, "years old.")

#printing Types of the values
a = 9
b = 9.1
c = "Hello"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))


#Swap values of two variables and print them before and after swap
a = 2
b = 3
print("Before swap")
print("a = ", a)
print("b = ", b)
a,b = b,a
print("After swap")
print("a = ", a)
print("b = ", b)

#swap 2 numbers with using temporary variables
a = 2
b = 3

temp = a
a = b
b = temp

print("a = ", a)
print("b = ", b)


#Read two numbers as input strings, convert them to integers, and print their sum
a = '1'
b = '2'
print(int(a)+int(b))

#Convert float to integer and print both values
a = 1.22
b = int(a)
print(b + a)

#Input an integer and print it as a string and float
a = int(input())
print(str(a))
print(float(a))

name = 'Jaya'
age = 21
city = 'Hyderabad'
print("Hi ", name, "you are ",age,"years old and live in ",city)

#Input two numbers and perform all arithmetic operations (+, -, *, /, %, **)
a = 8
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

#Print function
n = int(input())
for i in range(1,n+1):
    print(i, end="")



#Leap year or not
def is_leap(year):
    leap = False

    if(year%4==0):
        if(year%400 == 0) or (year%100 != 0):
            leap = True
    return leap

year = int(input())
print(is_leap(year))


#swapcase a string
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#capitalize the first letter of words
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return s.title()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

#using function with f strings
def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first_name} {last_name}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


#print even numbers
n = int(input())
for i in range(0, n):
    if i%2==0:
        print(i)

#print odd numbers
n = int(input())
for i in range(0,n):
    if(i%2 != 0):
        print(i)