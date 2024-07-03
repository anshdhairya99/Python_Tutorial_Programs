#--------------------------------- Decorators In Python👇:------------------------------------------

def function1():
    print("Subscirbe Now!")

func2 = function1
del function1
func2()

def funcret(num):
    if num==0:
        return print
    if num ==1:
        return int
a = funcret(0)
print(a)

def funcret(num):
    if num==0:
        return print
    if num ==1:
        return sum
a = funcret(1)
print(a) 

def executor(func):
    func("this")
executor(print)

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed")
    return nowexec

@dec1   # this is mainly is decorators. 
def who_is_harry():
    print("Harry is a good boy")

#who_is_harry = dec1(who_is_harry)
who_is_harry()



@dec1
def who_is_ansh():
    print("Ansh is good boys!")
who_is_ansh()