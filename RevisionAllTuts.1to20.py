# Revision Of All Tuts. from 1 to 20 Basic to Advance Level :-------------------------------

 # Built In Modulus :--

print("Hello Google🌎")

# Single line Comment:--
# Hello Google

# Multiple Line of Comment:---
"""hello 
google
my 
name 
is 
alexa"""

# Used of (end):---
"""print("Hello",end=" ")
print("Google😊")"""

# Escape Sequence character :--
"""print("C:\harry") 
print("C:\narry") # its \n except the new line character .
print("C:\\narry")
print('C:\Ansh')
print("Harry is the \t good boy")"""
# Concatinate the string if we are add the two strings:---
# string(name)+string(name) = (concatinate)

# Variables:--------- 
"""var1 = "hello Roman"
print(var1)
var2 ='ram'
var3 ='share ne'
print(var2+var3)"""

"""var4 = 'Rohan' #or " " 
var5 = '45'
print(var4+var5)"""

"""var6 = 'Roman Reings'
var7 = 900 # it is concatinate the string not print the used the str.
print(var6+var7)"""

"""var8 = 'Ikka'
var9 = '1'
print(var8+var9)"""

"""var1 = "hello"
var2 = 45
var3 = 45.99

#print(var1+str(var2))
print(var1+str(var3))
print(var2+var3)
print(var3+var2)"""

var1 = "Roman"
var2 = "Reings"
var3 = "34"
var4 = "99.99"
var5 = "23"
print(var1+var2)
print(var2+var3)
print(var4+str(var5))
print(str(var5)+var1)
print(var2+var3)
print(int(var5)+int(var3)) # In which the add the number.

# Data Types:-----

var6 = "hello"
var7 = "4"
var8 = 55.34
print(type(var6))
print(type(var7))
print(type(var8))
print(var6+var7)
print(var6+str(var8))
print(str(var8)+var7)
print(var7+str(var8))

# Type Casting:-----

var5 = "23"
var6 = "11"
print(int(var5)+int(var6))

var2 = 4
var6 = 11
var1 = "hello Digipods"
var6 = 11
var7=12
print(10*int(var2)+int(var6))
print(10*str(var1)+str(var6))
print(100*int(var2)+100*int(var7))


# Add of  the number:--

print("Enter the number")
num = int(input())
print("You entered",int(num)+10)

# Multi  of the Number :---
print("Enter the Number are you want that")
num = int(input())
print("You Entered",int(num)*100)

# Subract of the number:--
print("Enter the number")
num = int(input())
print("You entred",int(num)-500)

# Make the calculator in which add the two number:--

print("Enter the first number")
num1 = int(input())
print("Enter the Second number")
num2=int(input())
print("Sum of the two number are",int(num1)+int(num2))

# String In Python:-----

mystr = "Harry is the good boy"
print(mystr)

mystr = "Roman Reings"
print(mystr[0])
print(mystr[1])
print(mystr[0:12])
print(mystr[0:15])

# String Slicing :----

mystr = "Harry potter onnof the my fovrate"
print(mystr[0:5])
print(mystr[0:13])
print(len(mystr))

mystr1 = "Hey! Aleena I loved  it your eyes"
print("The length of",len(mystr1))
print(mystr1[0:34])

mystr3 = "kamal play chess"
print(len(mystr3))
print((mystr3[0:100]))

# Advance Slicing:---

mystr5="Hello Boys Whats UP!"
print("This is length",len(mystr5))
print((mystr5[0:5:2])) # skip the indexing from front
print(mystr5[::948])
print(mystr5[:]) # print all mystr5
print(mystr5[::])# ""
print(mystr5[0:])# ""
print(mystr5[:5]) # came only first varaible hello
print(mystr5[0:19:1])  # all string print it.
print(mystr5[::2]) # it skip the variable from front

# Advance Negative Indexing :----

mystr10 = "Dwane Johnson is the best wresthlar"
print(len(mystr10))
print(mystr10[:])
print(mystr10[-1:0])
print(mystr10[-4:0])
print(mystr10[-4:-2])
print(mystr10[:23])
print(mystr10[0:1])
print(mystr10[::1])
print(mystr10[0:-3])
print(mystr10[::-1]) # it has opposite the mystr10

# True and False :----

"""mystr = "12345"
print(mystr.isalnum()) # isalnum exclude of numeric
print(mystr.isalpha()) # it is exclude of character and numeric.
print(mystr.capitalize()) # it is not capatilize because it is an numerical order
print(mystr.split()) # split function change in list.
#print(mystr.join()) # it is join the string in one.
print(mystr.endswith(5))
print(mystr.strip()) # remove the space"""

# Formatting Methods :---

list1 = "HeyJohnWherearelivigatthIstime"
print(len(list1))
print(list1)
print(list1.capitalize()) # it is first letter is capital.
print(list1.title()) #  all the  first letter  in string.
print(list1.upper())  # all the character in upper letter.
print(list1.lower()) # all letter in lower .
print(list1.swapcase())
print(list1.isspace())
a = list1.replace('Hey','Hello') # it helps to replace the character from other char.
print(a) 
b=list1.split() #this pieces returns in list. 
print(b)
g=''.join(list1)
print(g)

h = list1.strip()
print(h)

# LIST IN PYTHON :-----------------------
grocery = ["Harpic","Vim bar","Deodrant","Cooler","Lollypop",56]
print(grocery)
print(type(grocery))
print(grocery[5])

# Python List And List of Function:----

numbers= [10,9,4,8,6,7,5,3,2]
print(numbers)
print(numbers[5])

# Sorting The Number:--

numbers.sort()
print(numbers)

# Reverse the numbers :---

numbers.reverse()
print(numbers)

print(numbers[1:5])
print(numbers)

#Excluding fn & skip function:---
print(numbers[::2])

# Negative slicing String :----

print(numbers[::-3]) # it skip the -3 from the last
print(numbers[1:5:-3])
print(numbers[1:5:2])
print(numbers[1:5:2])

# Used the string:--
print(len(numbers))
print(min(numbers))
print(max(numbers))
 # Append they are add the no. behind the integer;

numbers.append(55)
numbers.append(56)
print(numbers)

# Indexing No. 
numbers.insert(5,99) # the number 99 stand on behalf of index 5
print(numbers)

# Remove the no. from the table:---

numbers = [2,3,4,5,6,7,8,9,10]
numbers.remove(5) # it is remove the 5 from the list.
print(numbers)

# pop the no. from the table;
numbers.pop()
print(numbers)
numbers[1]=88
print(numbers)

# Tuples :---

tp = (1,2,3,4,5,6,7,8,9,10)
tp =(1)
print(tp)

a= 1
b = 2
a,b=b,a
print(a,b)
print(b,a)

# Mutable - can change (our list is mutable)
# immutable - can not change (our tuple is immutable)

# Dictionary & its function :-----

d1 = {}
print(type(d1))

d2 = {"Harry":"Burger","Ansh":"Pizza","Shreya":"Choclate","Shubham":"Chowmein","Rohan":"Fish","Rama":{"B":"Whole Egg","L":"Dal Chaval","D":"Some Whole Mutton"}}
print([d2])

print(d2["Ansh"])
print(type[d2])

print(d2["Rama"]["B"])
print(d2["Rama"]["L"])
print(d2["Rama"]["D"])

# find the dictionary of every person :---
print(d2["Shreya"])
print(d2["Ansh"])
print(d2["Harry"])

# Add the string in d2 and you also add the number :===
d2["John"] = "Junk Food" 
d2["Anas"] = "Seak Kabab"
d2["776"] = "234"
d2["567"] = "678"
print(d2)

# When you want to delete any function :---

del d2["776"]
print(d2)

# Dictionary fn. you want that copy fn--

d3 = d2.copy()
d3 = d2
del d3["Ansh"]
print(d2)
print(d2.get("Ansh"))

# Update the function :---

d2.update({"Ansh":"Tofee"})
print(d2.keys())
print(d2.items())

car = {
    "brand":"Bugati",
    "model":"chiron",
    "year":"1930"
}
car.popitem()
print(car)

bike = {
    "Brand":"Mercedes",
    "Model":"AMG G63",
    "year":"1957"
}
bike.popitem()
print(bike)

cycle = {
    "Brand":"BMW",
    "Model":"BMW2000",
    "year":"1923"
}
cycle.popitem()
print(cycle)


"""dict1 = {"Ansh":"Rojar","Hello":"friend","Gopal":"Bike","Ram":"Shyam"}
dict1.clear()
dict1.copy()
dict1.fromkeys()
dict1.get()
dict1.items()
dict1.pop()
dict1.popitem()
print(dict1)
print(dict1)
print(dict1)
print(dict1)
print(dict1)"""

#  create the dictionary and taken from the user and return the meaning of the word from the dictionary.

d3 = {"SET":"Set is the whole of the variable and character",
      "TABLE":"A table is the there are many numbers are in table",
      "VARAIBLE":"A variable is a collection of character",
      "ALPHABETS":"A Alphabets is the collection of Alphabets",
      "MOUSE":"Mouse the hardware in which we move the cursor"}
print('Enter the Any word for Meaning')
num = input()
print(d3[num])

# set :------------------------

s = set()
print(s)
print(type(s))
l = [1,2,3,4,5]
s_from_list=set(l)
print(s_from_list)
print(type(s_from_list))
s.add(1)
s.add(1)
print(s)
s.add(2)
print(s)
s.add(1)
s.add(2)
s1=s.intersection({1,2,3})
print(s,s1)
s1 = s.union({1,2,3})
print(s1)

s3 = {1,2,3,4,5,6,7,8,9,10}
s2 = s3.intersection({1,2,3,4,12}) # intersection are the only match value in s3.
s4 = s3.union({1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}) # all value came in one set.
print(len(s3))
print(len(s4))
print(s4)
print(s2)
print(max(s3))
print(max(s4))
print(s.isdisjoint(s3))
print(s)

# CONDITION STATEMENT IN PYTHON :------------------------------
# IF, ELIF, ELSE IN CONDITION ----------------

# 1:- Condition Of If Statement :--

a = 1000
b  = 5000
if b>a:
    print("B is greater than a ")

# 2:--
Rohanage = 98
John = 54
if Rohanage>John:
    print("Rohan is greater than John")

# 3:--
age = 100
ageram = 50
if ageram<age:
    print("ageram is less than age") 

# ELIF CONDITION :---
a = 33
b= 33
if a>b:
    print("It is grater than a")
elif a==b:
    print("It is both of the equal")    

age = 90
ageman= 80
if age>ageman:
    print("Greater")
elif age==ageman:
    print("Equal") 

# ELSE CONDITION :---

ram =23
shyam = 20
rohn = 18
kam = 18
if ram>rohn:
    print("Greater")
elif rohn==kam:
    print("Equal")
else:
    print("Not!!")

a = 200
b = 33
if b>a:
    print("b is greater than a")
elif a== b:
    print("a and b are equal")
else:
    print("a is greater than b")

a = 200
b = 33
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# We also used the some another condition as like:--
#AND,OR,NOT,NESTED IF, THE PASS STATEMENT-----------
# And:-- if one condition is false then answer came false
a = 200
b = 33
c = 500
if a>b and c>a:
    print("Both the condition are True")

# Or:--
a = 200
b = 33
c = 500
if a>b or a>c:
    print("At least one of the condition is true")
# Not :--

a =33
b= 200
if not a>b:
    print("a is not greater than b")

# Nested if :--
x = 41
if x>10:
    print("Above ten")
if x>20:
    print("And Also above 20")
else:
    print("But not above 20") 

# The pass statement:--- It gives the blank screen.
a = 33
b  =200
if b>a:
    pass

# QUIZ:--------------
print("Whats your age")
age = int(input())
if age<18:
    print("You can not  drive")
elif age==18:
    print("We will depend on body")
else:
    print("you can   drive")

# Python For Loops:----

"""fruits = ["Apple","Banana","Cherry"]
for x in fruits:
    print(x)"""

sabji = ["Bhindi","Gobhi","Aloo"]
for x in sabji:
    print(x)

"""list1 = [["Harry",1],["Ansh",2],["Chintoo",3]]
dict1 = dict(list1)
for item in dict1:
    print(item)"""
list6 = [["Ansh",200],["Gopal",500],["Hello",400]]
dict5 = dict(list6)
for x in dict5:
    print(x)


list1 = [["Harry",1],["Ansh",2],["Chintoo",3]]
for item , lollypop in list1:
    print(item,"and lolly is",lollypop)

items = [int,float,"Ansh","Kamil",45,5,8,34,2,66,99]
for item in items:
    if str(item).isnumeric()and item>=6:
        print(item)    

# Looping through a string:--
for x in "banana":
    print(x)    
    
# Break Statement :---

fruits = ["Apple","Banana","Orange","Pumpkin"]
for x in fruits:
    print(x)
    if x == "Banana":
     break

# Continue Statement :--

fruits=["apple","banana","cherry"]
for x in fruits:
    if x =="banana":
        continue
    print(x)

# Range of the Function:--

for x in range(1,6):
    print(x)

# Else in for loop:----

for x in range(6):
    print(x)
else:
    print("Finally Finished")


for x in range(6):
    if x==3:break
    print(x)
else:
    print("Finally Finished!")

# Nested Loops:---

"""adj = ["red","big","tasty"]
fruits=["apple","banana","cherry"]
for x in adj:
    for y in fruits :
        print(x,y)"""

adj = ["Yellow","Blue","Black"]
fruits = ["Pink","Red","Purple"]
for x in adj:
    for y in fruits:
        print(x,y)  

# Pass Statement :--

for x in [0,1,2]:
    pass

# WHILE LOOP IN PYTHON:--------

i = 1
while i<6:
    print(i)
    i+=1 

# Break Satement :---

i = 1
while i<5:
    print(i)
    if i==3:
        break
    i+=1
    
#The Continue Statement:---

m = 0
while m<10:
    i+=1
    if m==7:
        continue
    print(i)

# The else Statement:-----------------

"""n = 1
while n<6:
    print(n)
    i+=1
else:
    print("i is no longer less than 6")"""

# Quiz :-----------------
# To make a input from user untill the greater of 100 then say congrats if you give the below the no. of 100
# then say try again!!

while(True):
    a = int(input("Enter the Number"))
    if a>100:
        print("Congrats you have entered a number greater than 100\n")
        break
    else:
        print("Try Again")


# Exercie :

number_of_guesses = 18
print("No. of guesses is limited only a times")
while(number_of_guesses<=9):
    guess_number = int(input("Guess the no."))
    if guess_number<18:
        print("You enter less no. please input greater no.")
    elif guess_number>18:
        print("You enter greater number please input smaller no.")
    else:
        print("you won\n")
print(number_of_guesses,"no. of guesses he took to finish")
if(number_of_guesses>9):
    print("Game Over!!") 
 













