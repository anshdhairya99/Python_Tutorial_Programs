#---------------------------------- Map Filter & Reduce In Python:--------------------------------------------------

######---------------------------------------- MAP Function :-----------------------------------------

# -----------------------------------Using Of map with Range Function In Python:------------------------

numbers = ["3","34","64"]
numbers = list(map(int,numbers))

for i in range (len(numbers)):
    numbers[i] = int(numbers[i])

numbers[2] = numbers[2] + 1
print(numbers[2])
 

numbers1 = ["3","34","64","12"]
numbers1 = list(map(int,numbers1))
for i in range (len(numbers1)):
     numbers1[i] = int(numbers1[i])
numbers1[3] =numbers1[3] + 1
print(numbers1[3])

numbers = ["12","23","45","55","88"]
numbers = list(map(int,numbers))
for i in range(len(numbers)):
     numbers[i] = int(numbers[i])
numbers[4] = numbers[4] + 20
print(numbers[4])

numbers1 = ["44","22","88","77","100","200"]
numbers1 = list(map(int,numbers1)) 
for i in range(len(numbers1)):
     numbers1[i] = int(numbers1[i])
numbers1[5] = numbers1[5] + 100
print(numbers1[5])

# ------------------------Using of Map with Square Function In Python:-------------------------------------------- 

def sq(a):
    return a*a
num = [2,3,5,6,76,3,3,2]
square = list(map(sq,num))
print(square) 

def sq(a):
      return a*a
num = [2,3,4,5,6,76,3,3,2]
square = list(map(sq,num))
print(square)

def sqaure(a):
      return a*a
num = [2,3,4,5,6,7,8,9,10]
square = list(map(sqaure,num))
print(square)


#---------------------------------------- Using Of  Map with Lambda Function In python:---------------------------------

num = [2,3,4,5,6,77,88,7,8,3]
square = list(map(lambda x : x*x ,num))
print(square)



def square(a):
    return a*a
def cube(a):
    return a*a*a
func = [square, cube]
num = [2,3,4,5,6,77,3,3,2]
for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)

num2 = [2,3,4,4,5,6,7,8,12,10]
square = list(map(lambda x :x*x,num2))
print(square)

def square(a):
    return a*a
def cube(a):
        return a*a*a
func = [square,cube]
num = [2,3,4,5,6,7,7,8,9,10]
for i in range(10):
        val = list(map(lambda x:x(i),func))
        print(val) 
#------------------------------------------- FILTER Function :-------------------------------------------------------

list_1 = [1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
        return num>5
gr_than_5 = list(filter(is_greater_5,list_1))
print(gr_than_5)



list_6 = [12,33,3,3,44,5,5,6,11,111]
def is_greater_6(num):
        return num>6
gr_than_6 =(filter(is_greater_6,list_6)) # It has been print the filter object of the address.
gr_than_6 = list(filter(is_greater_6,list_6))
print(gr_than_6)

#----------------------------------------------REDUCE FUNCTION:-------------------------------------------------

from functools import reduce
list3 = [1,2,3,4,7]
num = reduce(lambda x,y:x+y, list3)
# num = 0
# for i in list3:
#         num = num+i
print(num)


from functools import reduce
list4 = [1,2,3,4,5,6,7,8,9,10]
num = reduce(lambda x,y:x*y,list4)
print(num)

