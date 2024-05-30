# Operators in Python:---

"""1. Arithmatic operators
2. Assignment Operators
3. Comparision Operators.
4. Logical Operators.
5. Identity Operators.
6. Membership Operators.
7. Bitwise Opearators"""

#1. Arithmatic Opearators:-- It is perform in the mathmatical operators:--
"""
x = 10
y = 12
print(x+y)

x = 12
y = 10
print(x-y) 

x = 20
y = 15
print(x*y)

x = 24
y = 12
print(x/y)

# It defines the remainder of the the divide.
x = 30
y = 15
print(x%y)

x  = 30
y = 15
print(x**y)
"""

"""print("5+6 is",5+6)
print("5-6 is",5-6)
print("5*6 is",5*6)
print("5//6 is",5/6)

# 2.Assignment Operators:-- Assign the value to variable.

print("Assignment Operators")
x = 5
print(x)
x+=7
print(x)

x = 20
print(x)
x-=10
print(x)


x = 30
print(x)
x*=10
print(x)

x = 50
print(x)
x/=20
print(x)

x = 40
print(x)
x%=10
print(x)

x = 40
print(x)
x//=20
print(x)

x = 70
print(x)
x**=20
print(x)

x = 50
print(x)
x&=20
print(x)

x = 20
print(x)
x|=20
print(x)

x = 10
print(x)
x^=12
print(x)

x = 10
print(x)
x>>=10
print(x)

x = 12
print(x)
x<<=12
print(x)


# Comparision Operators:-----------

i  = 12
print(i==12)

m = 10
print(m==5)

n = 20
print(n!=20)

k = 34
print(k>23)

k = 34
print(k<23)

o = 100
print(o>=120)

o = 120
print(o>=120)

s = 12
print(s<=10)
print(s<=12)"""

# Logical Operators:---------------------------

"""a = True
b = False
print(a and a)
print(a and b)
print(b and a)
print(b and b)
print(a or a)
print(a or b)
print(b or a)"""

# Identity Operators:---

"""x = 12
y = 10
print(x is x)
print(x is y)
print(x is not x)
print(x is not y)"""

# Membership Operatorsw:--

"""list = [2,3,3,4,5,6,6,7,1,2,3,4]
print(3 in list)
print(3  not in list)
print(12 in list)
print(12 not in list)"""

#Bitwise Operators:--

# 0- 00
# 1 -01
# 2 - 10
#3 - 11
"""print(0 & 2)
print(0 | 3)

print(0^1)
print(0 << 1)
print(0 >>1)"""

# Short hand if else Notation:--

"""a = int(input("Enter the number a\n"))
b = int(input("Enter the number b\n"))

if a>b: print("A bada hai bhai B se!")
else: print("B bada hai A se bhai")"""

# Function and Docstrings in Python:---

# In the python function are defined in def keyword:-

"""def my_function():
    print("Hello ffrom a function")
my_function()"""


# Function in python:--

# a = 9
# b = 10
# c = sum((a,b)) # built in function
# print(c)

# They are user define function:--

# def function1():
#     print("Hello Ansh you are in function1")
# print (function1())
# function1()

# def function2(a,b):
#     print("Are you in function2",a+b)
# print(function2(10,10))
# function2(20,20)

# To find the average :--

# def function2(a,b):
#     average = (a+b)/2
#     print(average)
#     return average

# v = function2(5,7)
# print(v)

# Find the Average of the number:--

# def function3(c,d):
#     average = (c+d)/2
#     #print(average)
#     return average
# f = function3(20,20)
# print(f)

# def function5(m,n):
#     sum = (m+n)
#     print(sum)
#     return sum
# k = function5(2,2)
# print(k)

# It is user define function and divide the number.
# def function6(l,b):
#     """This is the function which will calculate average of two numbers
#     They are the function of the first line is docstring"""
#     divide = (l+b)/2
#     return divide
#l = function6(20,20)
#print(l)
# print(function6.__doc__)

#Print the docstring in function:-

# def function7():
#     """This is the doc string are used in the function the first line o
#     under the function are doctstring"""
# print(function7.__doc__) 

# Try Except handling in Python:---

# print("Enter the first number\n")
# num1 = input()
# print("Enter the second number\n")
# num2 =input()
# try: 
#     print("Sum of the number is",int(num1)+int(num2))
# except Exception as e:
#     print(e)
# print("this line is very important")

# Try Except handling in python:--

# print("Enter the first num\n")
# num3 = input()
# print("Enter the second num\n")
# num4 = input()
# try:
#     print("Sum of the number is",int(num3)+int(num4))
# except Exception as e:
#     print(e)
# print("Hello voter you vote the any party you liked it.")


# File I/O Basic:--

# r - open file for reading. r is the default mode.
# w - open a file for writing
# x - ccreate file if not exist
# a - add more content to a file
# t - text mode
# b - binary mode
# + - read and write

# Question of the day:--

# def function44():
#     """This is the best way to read the docstring"""
# print(function44.__doc__)

# File Writing In Python:------------------------------------

# This function is used to open the any txt file.

# f = open("practice.txt")
# content = f.read()
# print(content)
# f.close() # It is used to close the file

# f = open("practice.txt","rb") 
# content =f.read(3)
# print(content)

# content =f.read(3)
# print(content)
 
# f.close()

# f = open("practice.txt","rt")
#content = f.read()
#for line in content: # it is read the one word in one line
 #   print(line)
# It is divide the letter in line wise:-
# for line in f:
    # print(line)
# print("1",content)
# content = f.read(23444)
# content = f.read(334454)
# print("2",content)
# f.close


# f = open("practice.txt","rt")
# print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read()
# print(content)

# file write in python :--

# f = open("HRX.txt","a")
# f.write("You are good in one")
# f.close()

# f = open("HRX.txt","r+")
# print(f.read())
# f.write("thank you\n")

# f = open("HRX.txt","a")
# a = f.write("Hey John what are you doing!")
# print(a)
# f.close()

# f = open("HRX2.txt","a")
# l = f.write("Hii")
# print(l)
# f.close()

# Pattern Printing:--

# print("How many rows you want to print")
# num =int(input())
# print("Type 1 or 0")
# two = int(input())
# new = bool(two)
# if new == True:
#     for i in range(1,num+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#             print()
# elif new == False:
#     for i in range(num,0,-1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#             print()

# More  on files:--

# f=open("HARRY2.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# f.close() 

# Seek in the python:------

# f = open("HARRY2.txt")
# print(f.readline())
# f.seek(10)
# print(f.readline())
# f.close()



# Using with block to open python file:--

# with open("marry.txt") as f:
#     # a = f.read(10)
#     # print(a)
#     f = open("marry.txt","rt")
#     f.close()    


