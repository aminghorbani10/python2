Lesson 1
print("Hello, World!")
#Lesson 2 Python Syntax
if 5 > 2:
  print("Five is greater than two!")
#Lesson 3
if 5 > 2:
 print("Five is greater than two!")
if 5 > 2:
        print("Five is greater than two!")
#Lesson 4 Python Comments
Comments starts with a #, and Python will ignore them:
#This is a comment
print("Hello, World!")
#Lesson 5 Python Variables
x = 5
y = "John"
print(x)
print(y)
#Lsson 6
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
#Lsson 7
a = 4
A = "Sally"
#A will not overwrite a
#Lsson 8 Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"
#Lsson 9 Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#Lsson 10 One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
#Lsson 11 Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#Lsson 12 You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#Lsson 13 For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)
#lesson 14 The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)
