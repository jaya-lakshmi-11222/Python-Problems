#Write a program using if to check if a number is positive
a=10
b=-1
if a>0:
    print('positive')
if b<0:
    print("negative")

#Write a program using if-else to check even or odd number
a=10
if a%2==0:
    print("Even")
else:
    print("Odd")

# Write a program to find the largest of two numbers using if-else
a=10
b=20
if a>b:
    print("a: ", a)
else:
    print("b: ", b)

# Write a program to find the largest of three numbers using if-elif-else
a=10
b=20
c=13
if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
else:
    print("c is largest")

#Write a program using nested if to check voting eligibility (age, citizenship)
age=20
citizenship="India"
if age>=18:
    if citizenship=="India":
        print("Eligible for Vote")
    else:
        print("Sorry not eligible because of citizenship")
else:
    print("Not eligible")

#Use if-elif-else to assign grades based on marks
marks=85
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("Grade F")

#Write a program to check if a number is divisible by both 2 and 3
a=18
if a%2==0 and a%3==0:
    print("It is divisible by 2 and 3")
else:
    print("Not divisible")

#Use nested if to check if a number is positive and even
a=10
if a>0:
    if a%2==0:
        print("Positive and Even")
    else:
        print("Not Even")
else:
    print("Not Positive")

#Write a program to check if a character is a vowel or consonant.
char1='a'
char2='b'
vowels='aeiou'
if char1 in vowels:
    print("Char1 is vowel")
if char2 not in vowels:
    print("Char2 is consonant")
else:
    print("Char2 is vowel")

# Write a program using if-elif-else to display the day of the week
day= 0
if day==1:
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
else:
    print("Sunday")

# Check if year is leap year or not
year =2025
if year%4==0:
    if year%400==0 or year%100!=0:
        print("Leap Year")
    else:
        print("Not a Leap year")
else:
    print("Not at all")

#Write a program to check if a number is a multiple of 3, 5, or both
a=15
if a%3==0 and a%5==0:
    print("Multiple of both 3 and 5")
elif a%3==0:
    print("Multiple of 3")
elif a%5==0:
    print("Multiple of 5")
else:
    print("Not a multiple of 3 or 5")

#Take a character input and check if it’s an uppercase letter (A–Z) without using built-in string functions
char1='A'
char2='a'
if char1>='A' and char1<='Z':
    print("Char1 is uppercase")
if char2>='A' and char2<='Z':
    print("Char2 is uppercase")
else:
    print("Char2 is lowercase")

#Use multiple if conditions to check if a number is divisible by any number other than 1 and itself
a=29
divisible=False
for i in range(2,a):
    if a%i==0:
        divisible=True
        break
if divisible:
    print("Not Prime")
else:
    print("Prime")

#Input coordinates (x, y) and determine in which quadrant the point lies (I, II, III, IV)
x = 10
y = -5
if x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
else:
    print("Quadrant IV")

#Determine whether a number is odd or even without using the modulus operator
num = 10
if (num // 2) * 2 == num:
    print("Even")
else:
    print("Odd")
