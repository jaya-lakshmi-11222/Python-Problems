#print 1 to 10 numbers
for i in range(1,11):
    print(i)

#print even number between 1 to 50
for i in range(1,51):
    if i%2==0:
        print(i)

#print multiplication table
n=int(input())
for i in range(1,11):
    print(n,"*",i,"=",n*i)

#print the sum of n numbers
n=int(input())
total=0
for i in range(1,n+1):
    total += i
print(total)