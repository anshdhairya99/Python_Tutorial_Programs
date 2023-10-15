# File Writing In Python:----

f=open("John.txt") # it comes in text form
content=f.read()
print(content)
f.close()

# All the text print
f=open("John.txt","r") # text print
content=f.read()
print(content)
f.close()

#It comes in binary form:--

f=open("John.txt","rb") # print the binary text
content=f.read()
print(content)
f.close()

# Read the character only

f = open("John.txt","rt") # text print
content=f.read()
print(content)
f.close()

# It also read only 5 character

f=open("John.txt")
content=f.read(5)
print(content)
f.close()

# Line wise character print

f=open("John.txt")
content=f.read()
for line in content:
    print(line)
    
# If you want print line:---

f = open("John.txt")
for line in f:
    print(line,end="")

# Readline Function  are multiple of lines read:--       

f = open("John.txt")
print(f.readline()) # it is print the first line
print(f.readline()) # it is print the second line
print(f.readline())
print(f.readline())
f.close()

# All line  print in list function

f=open("John.txt")
print(f.readlines()) # text print in the list.
f.close()