# Use the break & Continue Statement in python:---
"""i = 0
while (i<45):
    #print(1)
    print(i+1)
    print(i+1,end=", ")
    i=i+1"""
# Break Statement:-
"""i = 0
while(True):
    if i+1<5:
        i = i + 1
        continue
    print(i+1,end=", ")
    if(i==44):
        break
        #stop the loop
    i = i+1"""
#Break Statement:-----
"""i = 1
while i < 6:
  print(i)
  if i == 5:
    break
  i += 1"""
# Continue Statement:----
"""i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)"""


# Quiz 1-- To take input from user untill the big of 100.if the user have give the
#input below the 100 and then runned but if the give the big number of 100
#then say the user congrat.
"""while(True):
    inp = int(input("Enter the Number\n"))
    if inp>100:
        print("Congrats you have entered a number greater then 100\n")
        break
    else:
        print("Try again!")
        continue"""
#Some of the Programs of while loop in python:-
#Q1.Write a program to print the following using
#while loop
#A- First 10 even number....
"""num = 2
while(num<=20):
    print(num)
    num = num+2"""
# Q2:- first 10 odd number
"""num = 3
while(num<=30):
    print(num)
    num = num+3"""
# Q3:- first 10 natural number
"""num = 1
while(num<=10):
    print(num)
    num = num+1"""
#Q4:- first 10 whole numbers:-
"""num = 0
while(num<10):
    print(num)
    num = num+1"""
#Q5:- Write a program to print first 10 integer
#and their squares using while loop.
"""num = 1
print("Numbers Squares")
while(num<=10):
    print(num,num ** 2)
    num = num+1"""
#Q6:- Write for loop statement to print the
#following series:-
"""num = 10
while(num<=300):
    print(num,end= ", ")
    num = num+10"""
#Q7:- Write a while loop statement to print the
#following series.
"""num = 105
while(num>=7):
    print(num)
    num = num-7"""
#Q8:-write a program to print first 10 natural
#no. in reverse order using while loop
"""num = 10
while(num>=1):
    print(num)
    num = num-1"""
#Q9:- write a program to print sum of first 10 natural
#numbers
"""num = 10
sum = 0
while(num>=1):
    sum = (sum+num)
    num = num -1
    print(sum)"""
#Q10:- Write a program to print sum of first 10
#even numbers.
"""num = 2
sum = 0
while(num<=20):
    sum = (sum+num)
    num = num+2
    print(sum)"""
#Q11- Write a Program to print table of a number
# Entered from the user.

i = 1
num = int(input("Enter the table you want!"))
while i <= 10:
    print(num, " * ", i, " = ", num * i)
    i = i+1
