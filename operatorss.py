# OPERATORS IN PYTHON:--------------------------------------------------

# Arithmatic operators:-----------------------------
# Assignment Operators ------------
# Comparision Operators ---------
# Logical Operators--------------
# Identity Operators ---------------------------
# Membership Operators ------
# Bitwise Operators --------------------------

# Arithmatic operators :------------

print("5+6",5+6)
print("5-6",5-6)
print("5 * 6",5*6)
print("5 / 6",5/6)
print("5//6",5//6) #it is gives the integer (floar devision operators)
print("15%6",15%6) # it is gives the remainder 
print("5**6",5**6) # it is the (exponential operators)

# Assignment Operators :--------------------------------

print("Assignment Operators")
x=5
print(x)

x+=45
print(x)

x/=45
print(x)

x%=45 # x = x % 7
print(x)

x-=45
print(x)

x*=45
print(x)

x%=45
print(x)

x//=45
print(x)

# Comparision operators :------------

print("Comparision Operators")
i = 12
print(i==13)
print(i==12)
print(i!=12)
print(i>10)
print(i<13)
print(i>=12)
print(i<=15)

# Logical Operators :---

a = True 
b = False
c = True
d  = True
print(a and b)
print(d or c)
# And--
print("Logical Operators")
m = 20
print(m<12 and m>12) # If any one condition is false then false
print(m)
#Or--
print("Identity Operators")
m =30
print(m>17 or m<12)
print(m)
#Not---
h = 120
print(not(h<45)and(h<55))

# Identity Operators :---------

print("Identity operators")

a = True
b = False
print( a is b)
print(a is not b)

# Membership Operators--

print("Membership Oprators")
list = [3,3,4,5,77,22,99,100]
print(3 in list)
print(32 not in list)

# Bitwise Operators :----

print("Bitwise operators")
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11
# And --
print(0 & 1)
print(0 & 2)
# OR--
print(0 | 1)
print(0 | 2)

# X-or--
print(0 ^ 1)
print(0 ^ 2)
# Not ----
print( ~ 1)