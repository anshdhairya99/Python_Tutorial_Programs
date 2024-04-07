# List In Python:------------------

"""grocery=["Vim bar","Detergent","Deodrant","Soda","Bru-Gold"]
print(grocery)
print(type(grocery))
print(grocery[4])

# python list and list of the function:------

number=["12","33","45","66","78","100"]
print(number)
print(type(number))
print(type[number])
print(number[3])

#Sorting the number:---

number.sort()
print(number)

#Reverse the number::---

number.reverse()
print(number) 

print(number[1:5])
print(number)

#Excluding and Skiping the function:---
print(number[::3])
print(number)
"""
#Negative Slicing Function:-------

number=["12","13","77","99","100"]
print(number[1:3:])
print(number[2:4])
print(number[::9])
print(number[5::])
print(number[::5])
print(number[::2]) # It is skip the function from behind.
print(number[::]) # all the strings are print.
print(number[-5:2])
print(number[0:-2])
print(number[::5])


list2 = [00,44,99,77,33,55,22,11,10,99]
list2.append("22")
print(list2)

list2.clear()
print(list2)

list2.count(99)
print(list2)

list2.insert(22,14)
print(list2)
print(list2)

# remove the number from the table:----

list5 = [2,3,4,5,6,7,8,9,10]
list5.remove(10)
print(list5)

list5.remove(3)
print(list5)

list5.pop()
print(list5)
list5[1]=88
print(list5)


# Tuples In Python:--------
#Tuples are immutable it can not be changed.

tp = (1,2,3,4,5,6,7,8,9,10)
print(tp)

# If the tuples are immutable then it can not used.
a =12
b =23
a,b=b,a
print(a,b)
print(b,a)

# Dictionary in the Python:-----------

d1={}
print(type(d1))

d2={"Ansh":"Mango Juice","Gopal":"Orange","Arun":"Ice-Cream","guuloo":{"B":"Dinner","K":"Josh","L":"Logo"}}
print(d2)

print(type(d2))
print(type[d2])

print(d2["Ansh"])
print(type[d2])

print(d2["guuloo"]["B"])
print(d2["guuloo"]["K"])
print(d2["guuloo"]["L"])

# Find the dictionary of the each person:-------------------------

print(d2["Ansh"])
print(d2["Gopal"])
print(d2["Arun"])

# Add the strings and number in dictionary:---

d2["Jin"]="kallo"
d2["Bapu"]="kimmat"
d2["Limited"]="hole"
d2["345"]="899"
d2["900"]="1000"
d2["1200"]="5000"
print(d2)

# Some Method in Dictioanary:---

# This function have delete the 1200 in dictionary:-----------------
del d2["1200"]
print(d2)



d3 = d2.copy()
d3 = d2
del d3["Ansh"]
print(d2)
print(d2.get("Ansh"))


"""d4 = d2.copy()
d4 = d2
del d4["Arun"]
print(d2)
print(d2.get("Gopal")) 
print(d2.get("guuloo"))"""

"""d5 = d2.copy()
d5 = d2
del d5["Ansh"]
print(d5)
print(d2.get("Arun"))
print(d2.get("Gopal"))
"""

d2.update({"Ansh":"Mango Juice"})
print(d2.keys())
print(d2.items())


# It is also add the in the d2 function:---
car ={
      "brand":"Bugati",
      "Company":"Lamborgini",
      "year":"1970's"
}
car.popitem()
print(car)

bike={
      "brand":"Ninja h2R",
      "Company":"Kawasaki",
      "Model":"1940"
}
bike.popitem()
print(bike)

dict2={"Ansh":"Rojgar","Anoo":"Berojgar","Shreya":"Student","Lina":"La Maire Rosien"}
dict2.clear()
dict2.copy()
#dict2.fromkeys()
dict2.get("Ansh")
dict2.items()
dict2.keys()
#dict2.pop()
#dict2.popitem()
#dict2.setdefault()
dict2.update()
dict2.values()
print(dict2)
print(dict2)
print(dict2)
print(dict2)
print(dict2)
print(dict2)
print(dict2)
print(dict2)
print(dict2)
print(dict2)
print(dict2)



d7={
    "Set":"A Set is the function in which set the number from the data",
    "Table":"A table in which the number of rows and coloumn are in the same form",
    "Variable":"A Variable in which the collection of the characters",
    "Mouse":"A Mouse is the hardware in which the we move the cursor around it."
}
print("Enter the number are you want that in the row")
num =input()
print(d7[num])

# Set in Python:-------------------------------

s =set()
print(s)
print(type(s))

m =[1,2,3,4,5,6,7,8,9]
s = set(m)
print(s)

# Set In Python:---------------------------------------------------------------------

s = set()
print(s)
print(type(s))

l = [1,2,3,4,5]
print(type(l))
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

# Some Methods of Sets:---

s =([1,2,3,4,5])

print(type[s])

s.clear()
print(s)
s.copy()
print(s)
#s.pop()
#print(s)


# Intersection are the in which they are only number are print they have same in both the s3 and s4.
s3={1,2,3,4,5,6,7,8,9,10,1,1,12,2,3,4,5,6,7}
s4=s3.intersection({1,2,3,4,4,5,6,7})
print(s4)

#Union are the in which they are come the all number have print it.
"""s3={1,2,3,4,5,6,7,8,9,10,1,1,12,2,3,4,5,6,7}
s5=s3.union({1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20})
print(s5)
print(len(s3))
print(type(s3))
print(max(s3))
print(max(s5))
print(s.isdisjoint(s3))
print(s)"""


# CONDITION STATEMENT IN PYTHON :------------------------------
# IF, ELIF, ELSE IN CONDITION ----------------

# If statment are used-

a = 200
b = 300
if a<b:
    print("a is less then b")
    

a = 500
b = 1000
c = 1000
if b>a:
    print("b is greater than a")

if b==c:
    print("B&C is equal")

ansh = 123
anoo = 234

if anoo>ansh:
    print("anoo is greater than ansh")


#Elif Statement in Python:------

d = 1200
e = 1000
f = 1200

if d>e:
    print("d is greater than e")

elif d==e:
         print("if d is eual to e then print it.")


# Else Statement in Python:----

m = 1000
n = 2000
if m<n:
     print("n is greater than m")
elif m==n:
     print("M and N bothe are equal then print it.")

else:
     print("Not equal then print it.")


p  = 900
q = 100

if p>q:
     print("p is greater than the q")

elif p==q:
     print("If p and q are equal then print it.")

else:
     print("Not Matched!")

# We also used the some another condition as like:--
#AND,OR,NOT,NESTED IF, THE PASS STATEMENT-----------
# And:-- if one condition is false then answer came false

# Using of or only one condition is true. 
a = 123
b  = 234
if a>b or b>a:
     print("b is greater then a")

# Using of and only one condition is true:---
p = 500
d = 1000
if p>d and d>p:
     print("Only")     

# Not the condition is used:--

k = 1600
m = 1300
if  not k<m: # It is gives the opposite answer because they are used the not condition in python.
     print("if the condition is true then print it.") 

l = 1200
m = 13000
if m>l:
    pass

# Question Quiz:-------------

print("What's your age!")
age =int(input())
if age<18:
    print("You can not drive it!")
if age==18:
    print("When we suggest it!")
else:
    print("You can drive it!")

# Python In Loops :----------------------------

fruits = ["Apple","Orange","Banana"]
for i in fruits:
     print(i)

vegetable =["Bhindi","Gobhi","Shima-Mirch"]
for i in vegetable:
     print(i)

list = [["Lina",1],["Rodes",2],["Harry",3],["Sherni",4],["Marry",5]]
dict5 = dict(list)
for x in dict5:
    print(x)

list10 = [["Ortan",123],["Kapila",234],["Mouse",890],["Cghe",789]]
dict12 = dict(list10)
for x in list10:
    print(x)    
        

list88 = [["Ortan",123],["Kapila",234],["Mouse",890],["Cghe",789]]
dict13 = dict(list88)
for x in dict13:
     print(x)


items = [int,float,"Ansh","Kamil",45,5,8,34,2,66,99]
for item in items:
    if str(item).isnumeric()and item>=6:
        print(item)    


items2 = [int,float,"Dhairya","Living",77,99,34,12,75]
for item in items2:
     if str(item).isnumeric() and item>=6:
          print(items2)