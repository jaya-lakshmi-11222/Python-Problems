#right angled triangle pattern
n = int(input("Enter:"))
for i in range(0,n+1):
    print("*"*i)


#n rows and n columns pattern
n = int(input())
for i in range(0, n):
  for j in range(0, n):
    print("*", end=" ")
  print()


#Down right angled triangle pattern
n = int(input("Enter:"))
for i in range(n, 0, -1):
    print("*"*i)