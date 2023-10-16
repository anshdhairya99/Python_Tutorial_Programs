
# EXERCISE 4 :-------------------------------------------------------------------------------
# Pattern Printing:--------------------------------------------

# input = Integer n
# Input = Integer
# Boolean = True or False

# True n = 5

# *
# **
# ***
# ****

# False n = 5

# ****
# ***
# **
# *

print("How many row you want to print")
num1 = int(input())
print("Type 1 OR 0")
num2 = int(input())
new = bool(num2)
if new ==True:
    for i in range(1,num1+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(num1,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()         



               
    

