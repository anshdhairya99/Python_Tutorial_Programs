# FUNCTION IN PYTHON:--------------------------------------------------------------------------

a = 9
b = 8
c = sum((a,b)) #Built in function.
print(c) 

def function19():
  print("Hello You are in Function 1")
print(function19())
function19() 

def function8(p,k):
  print("Hello You are in function 8", p+k)
function8(200,200)

def function (h,k):
  print("Hello World",h+k)
function(36,36)

def function(r,k):
  print("keep it real!!",r+k)
function(45,45)

def my_function():
    print("Helllo Don")
my_function()

def function2(b,c):
  average = (b+c)/2
  print(average)
  return (average)
v = function2(6,6)
print(v)

def function5(p,q):
  average = (p+q)/2
  print(average)
  return (average)
g = function5(90,90)
print(g)

def function10(m,k):
  print("Hello World!!")
  average = (m+k)/2
  print(average)
  return average
v = function10(20,20)
print(v)


def my_function():
  print("Hello From a function") 
my_function()

#Arguments :----
def my_function(fname):
  print(fname + "Refsnes")
my_function("E-mail")
my_function("Tobias")
my_function("Linus")

# Number of Arguments :--
def my_function(fname, lname):
  print(fname + " "+ lname)
my_function("Email","Refsnes")  

# Arbitrary Arguments *args :--
"""def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Email","Tobias","Linus") """ 

# Keyword Arguments :--
"""def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child3 = "Emil", child2= "Tobias", child1="Linus")"""

def myfunction2():
  print("Hello I'm at Dubai Down Town")
myfunction2()

def my_function55(a,b):
  average = (a+b)/2
  print(average)
my_function55(20,20)

def function(o,p):
  print("Sum of all the function is",o+p)
  average = (o+p)/2
  return average
v = function(55,55) # because we build the variable from v.
print(v)


# Doc Strings :--------------------------------------------------------------------------------

def my_function(p,k):
  """Hey Gabru What are you do that in Dubai Down Town
Im just coming for his work and Im live at Dubai at Tonight"""
  average = (p+k)/2
  print(average)
print(my_function.__doc__)

def function2(a,b):
  """This is function which will calculate average of two numbers
  this function does not work on the function"""
  average = (a+b)/2
  return average
print(function2.__doc__)

def my_function1(c,k):
  """HEy everyone what are you do that at this time
  the work has been valid for the function"""
  average = (c+k)/2
  return average
print(my_function1.__doc__)

# Arguments of function :--

def my_function(fname):
  print(fname + "Refrence")
my_function("Email")
my_function("Tobias")
my_function("Linus")


def my_function(fname):
  print(fname + "Refrence")
my_function("World")
my_function("Global")
my_function("Work")


# QUESTION ON FUNCTION WITH SOLUTION :------------------

# Write a Python function to find the maximum of three numbers.

def max_of_two(x,y):
  if x>y:
    return x
  return y 
def max_of_three(x,y,z):
  return max_of_two(x, max_of_two(y,z))
print(max_of_three(3, 6, -5))

# It is solve with single *args :-----
def func1(*args):
  for i in args:
    print(i)

func1(20, 40, 60)
func1(80, 100)

def calculation(a,b):
  addition = a-b
  subtraction = a+b

  return addition, subtraction
res = calculation(40,10)
print(res)

# function with default argument
def show_employee(name, salary=9000):
    print("Name:",name,"salary:", salary)
show_employee("Ben", 12000)
show_employee("Jessa")
              


def show_employee(name, salary=25000):
  print("Name:",name,"salary:",salary)

show_employee("Anil",25000)
show_employee("Rakesh")  


def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0

res = addition(10)
print(res)



def display_student(name, age):
    print(name, age)

# call using original name
display_student("Sahil", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("Russo", 26)

