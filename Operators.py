#Arithmetic operators
x=int(input())
y=int(input())
p = x+y
q = x-y
r = x*y
s = x//y
t = x%y
print(p, q, r, s, t)

#break

#Logical Operators
a=int(input())
b=int(input())
p = a and b
q = a or b
r = not a
print(p,q,r)

#break

#Bitwise operators
a=int(input())
b=int(input())
c=int(input())
d=a^a
e=c^b
f=a&b
g=c | (a^a)
e= ~e
print(d, e, f, g, sep=' ')

#break

#modulo task
N = int(input())
if N == 1:
    result = 1
else:
    result = (N // 2) + 1
print(result)

#break

#Last Digit of number
n = int(input("Enter a number: "))
last_digit = abs(n) % 10
print(last_digit)

#Last Digit of number using strings
n = int(input("Enter a number: "))
last_digit = (int(str(n)[-1]))
print(last_digit)

#break

#greatest common divisor(gcd)
import math
a = int(input())
b = int(input())
c = math.gcd(a,b)
print(c)

#Least common multiple(lcm)
import math
a = int(input())
b = int(input())
c = math.lcm(a,b)
print(c)

#break


