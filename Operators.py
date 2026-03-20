#Arithmetic Operators
a = 10
b = 2

print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print('a // b =',a // b)
print('a % b =', a % b)
print('a ** b =',a ** b)

#Comparision Operators
a = 10
b = 4

print('Two numbers are equal or not:', a == b)
print('Two numbers are not equal or not:', a != b)
print('a is less than or equal to b:', a <= b)
print('a is greater than or equal to b:', a >= b)
print('a is greater than b:', a > b)
print('a is less than b:', a < b)

#Assignment Operators
a = 34
b = 6

print('a += b:', a + b)
print('a -= b:', a - b)
print('a *= b:', a * b)
print('a /= b:', a / b)
print('a %= b:', a % b)
print('a **= b:', a ** b)
print('a //= b:', a // b)

#Logical Operators
a = 7
b=10
if a>b and a%2 != 0:
    print("a is greater and odd")
if b>a or b%2==0:
    print("b is greater or even")
if not(b<a):
    print("b is greater")

#Bitwise Operators
a = 7
b = 8

print('a & b :', a & b)
print('a | b :', a | b)
print('a ^ b :', a ^ b)
print('~a :', ~a)
print('a << b :', a << b)
print('a >> b :', a >> b)

#Membership Operators
list=[1,2,3,4,5,6]
if 3 in list:
    print("present")
if 9 not in list:
    print("Not Present")

#Identity Operators
a=5
b=5
if a is b:
    print("same")
if a is not b:
    print("Not Same")