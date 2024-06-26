# Map Filter & Reduce In Python:-------

###### Map Function :----

# Using Of map with Range Function In Python:----

# numbers = ["3","34","64"]
# numbers = list(map(int,numbers))

# for i in range (len(numbers)):
#     numbers[i] = int(numbers[i])

#numbers[2] = numbers[2] + 1
#print(numbers[2])

# Using of  map with Square Function In Python:-- 

# def sq(a):
#     return a*a
# num = [2,3,5,6,76,3,3,2]
# square = list(map(sq,num))
# print(square) 

# Using Of  map with Lambda Function In python:------

# num = [2,3,4,5,6,77,88,7,8,3]
# square = list(map(lambda x : x*x ,num))
# print(square)

# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# func = [square, cube]
# num = [2,3,4,5,6,77,3,3,2]
# for i in range(5):
#     val = list(map(lambda x:x(i),func))
#     print(val)
