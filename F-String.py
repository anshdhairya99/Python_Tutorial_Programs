# F-String In Python:------------------------------------------------

import math # python module math

me = "Strings"
a1 = 23
a = "This is %s %s" %(me,a1)
print(a)

me6= "Hii Canada"
a2 = 666
a5 = 999
k = "Public Supermacy %s %s %s" %(me6,a2,a5)
print(k)

me1 = "Hello Luknow??"
a2 = 450
a4 = 23
a5 = 45
b  = "Kya bolti Public %s %s %s %s" %(me1, a2, a4, a5)
print(b)

me = "Harry"
al = 3
a = "this is %s %s"%(me, a1)
a = "This is {1} {0}"
b = a.format(me, a1)
print(b)

ne = "Hello Jaat"
a5 = 90
h = "This is %s %s"%(ne,a5)
l = "This is {1} {0}"
j = l.format(ne,a5)
print(j)


# F-String to find the value in math:--------------------------------------------

a = f"This is {me} {a1} {math.cos(65)}" #the value of cos 65
print(a)

c = f"This is harry {me} {a1} {math.sin(30)}"
print(c)

k = f"This is the bad boy{me} {a5} {math.sin(90)}"
print(k)

o = f"Hello My name is daniel{me} {a5} {math.sin(60)}"
print(o)

p = f"My name is Kendra lust{me} {a2} {math.tan(90)}"
print(p) 