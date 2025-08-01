#basic print statement
print("Hello, World!")

#break

#sep and end concept
a = input()
b = input()
separator = input()[0]

# Print with space
print(a,b,sep=' ')

# Print without newline at the end
print(a,b,sep=' ',end='')

# Print with separator
print(a,b,sep=separator)

# Print without space
print(a,b,sep='')

#break

#Multiprinting
a = input()
n = int(input())
print(a*n,sep='')

#break

#Int Str
a = input()
b = input()
c = input()
# Write your code below that prints a a times and b b times, seperated by c
print(a*int(a),b*int(b),sep=c)

#break

#Taking Input
s=input()
n=int(input())
f=float(input())
print(s)
print(n+10)
print(f*10)

