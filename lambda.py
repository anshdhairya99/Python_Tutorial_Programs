# Lambda Function and Anonymous Function in python:----

def add(a, b):
    return a+b

minus = lambda x, y: x-y

def minus(x,y):
    return x-y

print(minus(9,4))
multiply = lambda x, y: x * y
print(multiply(3, 5))
 
# Sort Lambda function:----

def a_first(a):
    return a[1]


a = [[2,14],[5,6],[8,23]]
#a.sort(key=a_first)
a.sort(key=lambda x:x[1])
print(a)






