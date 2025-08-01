#Type conversion float to int
d = float(input())
print(int(d))

#break

#Typecast and double it
num = input()
print(int(num)*2)

#break

#swap the numbers
a = int(input())
b = int(input())
a,b=b,a
print(a, b)

#break

#Sum of n natural numbers
n = int(input())
total=0
for i in range(1,n+1):
  print(i)
  total += i
print(total)

#Sum of n natural numbers without using loops
n=int(input())
sum = n*(n+1)//2
print(sum)

