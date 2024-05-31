
# Local Variable:---------------------------------------------------

def function1(n):
    l  = 34 # local variable
    m = 33 # local variable
    print(l,m)
    print(n, "I have Printed")
function1("This is me")

# Global Variable:----------------------------------------------------

d = 12 #global variable
def function1(n):
    print(n,"I have Printed")
function1("This is me")
print(d)

# Global keyword:---------------------------------------------------

l = 10 # global
def function1(n):
    #l = 5 # local
    #m = 10 #local
    global l
    l = l+45
    print(l)
    print(n,"I have printed")
function1("this is me")


# Quiz:----------------------------------------------------------------

def harry():
    x  = 20
    def rohan():
        global x
        x = 99
    print("before calling rohan()",x)
    rohan()
    print("After callling rohan()",x)
harry()
print(x)


