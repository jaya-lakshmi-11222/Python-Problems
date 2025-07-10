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