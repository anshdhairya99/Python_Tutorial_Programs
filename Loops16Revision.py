# For Loop Some Qestion Probleum Solving:--

#1:- Write a program to print first 10 even numbers.

"""print("First 10 evem number are")
i = [2,4,6,8,10,11]
for i in range(1,11):
    print(i)"""

# 2:- Write a program to print first 10 natural no.
#print("First 10 natural number")

"""i = [1,2,3,4,5,6,7,8,9,10,11]
for i in range(1,11):
    print(i)"""

# 3-Write a program to print first 10 odd no.
#print("First 10 odd number")

"""i = [3,7,9,11,13,15,19,25,27,29,31]
for i in range(3,11):
    print(i)"""

# 4- Write a program to print first 10 even numbers in reverse order.

"""print ("First 10 even numbers in reverse order")
i = [20,18,16,14,12,10,8,6,4,2]
for i in range(20,0,-2):
    print(i)"""

# 5 - Write a program to print table of a number
#accepted from user.

"""print("Enter any number")
num = int(input())
for i in range(1,11):
    print(num*i)"""

# 5- Write a program to find the factorial of a number.

"""print("Enter any number")
num = int(input())
f = 1
for i in range(1,num+1):
    f = f*i
    print("factorial is",f)"""
# 6-
#Python program to illustrate--
"""list = ["geeks","for","geeks"]
for i in list:
   print(i)"""

# 7:--
# Iterating over dictionary
"""print("Dictionary Iteration")
d= dict()
d['XYZ'] = 123
d['ABC'] = 345
for i in d:
   print("%s %d" %(i,d[i]))"""
# 8:--
# Iterating over a string
"""print("String Iteration")
str = "Geeks"
for i in str:
    print(i)"""

# PYTHON FOR LOOPS:----
# PRACTICE:--
#SYNTAX:- for var in iterable:
#        statement
#1 -------------------

#fruits = ["apple","grapes","mango"]
#for x in fruits:
#    print(x)

#2:----------------------

#list1 = [["harry",1],["Ansh",2],["chintoo",500],["Gopu",450]]
#dict1 = dict (list1)
#for item in dict1:
  #  print(dict1)

#for item,lollypop in list1:
   # print(item,lollypop)

#for item,lollypop in list1:
   # print(item,"and lolly is",lollypop)
# 3----------------------------------------------

#items = [int,float,"Ansh","kamil",45,5,6,7,8,9,10,110,512,260]
#for item in items:
 #   if str(item).isnumeric() and item>=6:
  #      print(item)
# 5:-------------------------------
#LOOPING THROUGH A STRING:----
"""EX-
for x in "banana":
   print(x)"""

#BREAK STATEMENT:---
"""fruits = ["Apple","Banana","Cherry"]
for x in fruits:
     print(x)
     if x == "Banana":
         break"""
#when we used the break statement:-----
"""fruits = ["Apple","banana","cherry"]
for x in fruits:
    if x == "banana":
       break
    print(x)"""
#Continue Statement:---
"""fruits = ["Mango","Papaya","Watermelon"]
for x in fruits:
        if x == "Mango":
            continue
        print(x)"""
# The Range () Function:--
"""for x in range(0,11):
    print(x)"""

# Else in for loop:---
"""print("The value of you want that")
for x in range(0,77):
    print(x)
else:
    print("Finally Finished")"""
#Nested lopps:--- misslaneous grouping:----

"""adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)
adj = ["Black","Red","Brown"]
shoes = ["calcetto","redtape","puma","adidas","kappa","luis voilutton","skechers"]
for x in adj:
    for y in shoes:
        print(x,y)"""
    #the pass statement:----
    #for x in [0,1,2,3]
     #   pass

# having an empty for loop like this, would raise an error without the pass statement






