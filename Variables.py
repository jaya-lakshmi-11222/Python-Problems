# Create a variable to store your name and print it
name='Jaya'
print(name)

# Store two numbers in variables and print their sum
a=1
b=2
print(a+b)

#Swap two variable values using a temporary variable
a=5
b=10
temp=a
a=b
b=temp
print("a=",a, "b=",b)

# Swap two variable values without using a temporary variable
a=5
b=10
a,b=b,a
print(a,b)

# Assign the same value to multiple variables and print them
x=y=z=100
print(x,y,z)

#Create a variable of each type (int, float, str, bool) and print their types
a=10
b=1.0
c='prepare'
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Update a variable value and print before and after update
before=10
print('Before:', before)
after=20
print("After:", after)

#. Use multiple assignment to assign values in one line
a,b,c=1,2,3
print(a,b,c)

#. Concatenate two string variables and print the result
a='Hi'
b="Hello"
print(a+' '+b)

#Delete a variable using del and try to print it (observe error)
a=10
print(a)
del a
print(a)