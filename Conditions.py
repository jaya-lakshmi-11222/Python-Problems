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