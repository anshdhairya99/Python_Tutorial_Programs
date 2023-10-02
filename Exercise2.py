# QUIZ :---------------------------------------------------------

# Exercise 2---
# Faulty Calculator--
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
#Design a calculator which will correctly solve all the probleum except
#the following ones:-
#45 * 3 = 555, 56+9 = 77,56/6 = 4
#your program should take operator and the two numbers as input from the user and then result -

print('Enter 1st Number')
num1 = int(input())
print('Enter the 2nd Number')
num2 = int(input())
print("So what you want?'+','-','/','%','*'")
num3 = input()
if num1 ==45 and num2 ==3 and num3=='*':
    print("555")
elif num1 == 56 and num2 ==9 and num3 == '+':
    print("77")
elif num1 == 56 and num2 == 6 and num3 == '/':
    print("4")
elif num3=='*':
    num4=num1*num2
    print(num4)
elif num3 =='+':
    plus=num2+num1
    print(plus)
elif num3 =='/':
    Ansh=num2/num1
    print(Ansh)
elif num3 == '-':
    Ansh=num2-num1
    print(Ansh)
elif num3 == '%':
    percent=num2%num1
    print(percent)
else:
    print('Error! Please check your input')

#Do code with self-------------
#45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4,30-28  = 3,30%5 = 6


print('Enter the first number')
num1 = int(input())
print('Enter the second number')
num2 = int(input())
print("So want you want that?'+','-','/','%','*'")
num3 = (input())
if num1 ==45 and num2 ==3 and num3 =='*':
    print("555")
elif num1 ==56 and num2 ==9 and num3 =='+':
    print("77")
elif num1 ==56 and num2 ==6 and num3 =='/':
    print("4")
elif num1 == 30 and num2 == 28 and num3 == '-':
    print("3")
elif num1 == 30 and num2 == 5 and num3 == '-':
    print("7")
elif num3=='*':
    num4= num1*num2
    print(num4)
elif num3== '+':
    plus= num1 +num2
    print(plus)
elif num3== '/':
   Dev= num1/num2
   print(Dev)
elif num3== '-':
    Dev= num1-num2
    print(Dev)
elif num3 == '%':
    percent=num1%num2
    print(percent)
else:
    print('Error! Please check your input')

#REPEAT PROGRAM ----


#FAULTY CALCULATOR---

#45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4,30-28  = 3,30%5 = 6

print("Enter the first number")
num1 = int(input())
print("Enter the second number")
num2 = int(input())
print("So What You Want that?,'+','-','*','/','%',")
num3 = input()
if num1 ==45 and num2 ==3 and num3 =='*':
    print("555")
elif num1 ==56 and num2 ==9 and num3 =='+':
    print("77")
elif num1 ==56 and num2 ==6 and num3 =='/':
    print("4")
elif num1 ==30 and num2 ==28 and num3 =='-':
    print("3")
elif num1 ==30 and num2 ==5 and num3=='%':
    print("6")
elif num1 =='*':
    num4 = num1*num2
    print(num4)
elif num2 =='+':
    plus = num1+num2
elif num3 =='/':
    Ansh = num1/num2
    print(Ansh)
elif num3 =='%':
    Divide =num1%num2
    print(Divide)
else:
    print("Error! Please check the your input")

# QUIZ :------------------------
# FAULTY CALCULATOR--------------------------------
#45 * 3 = 555, 56 + 9 = 77, 56 / 6 = 4,30-28  = 3,30%5 = 6

print("Enter the First number")
num1 = int(input())
print("Enter the Second Number")
num2 = int(input())
print("So What You Want that- '+','-','*','%','/',")
num3 = input()
if num1 ==45 and num2==3 and num3=='*':
    print("555")
elif num1==56 and num2==9 and num3=='+':
    print("77")
elif num1 ==56 and num2==6 and num3=='/':
    print("4")
elif num1==30 and num2==28 and num3=='-':
    print("3")
elif num1 ==30 and num2==5 and num3=='%':
    print("6") 
elif num3=='*':    
    multi = num1*num2
    print(multi)
elif num3=='+':
    plus =num1+num2
    print(plus)
elif num3=='/':
    divide=num1/num2
    print(divide)
elif num3=='-':
    minus = num1-num2
    print(minus)
elif num3=='%':
    modulus = num1%num2
    print(modulus)
else:
    print("Error! you can check them")





