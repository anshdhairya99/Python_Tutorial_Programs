
# File Writing:----------------------------------------------

f = open("file.txt")
content = f.read()
print(content)
f.close()

# All the text file print ----------------------------------------------------------------

f  = open("file.txt","r")
content = f.read()
print(content)
f.close()

# It comes in binary form--------------------------

f = open("file.txt","rb")
content = f.read()
print(content)
f.close()
# Read the characters only ---------------------------------------------------------

f = open("file.txt","rt")
content = f.read()
print(content)
f.close()

# It also read te only 5 character------------------------------------------------------------------------

f = open("file.txt")
content =f.read(5)
print(content)
f.close() 

# Line wise character printed -------------------------------------------------------

f = open("file.txt")
content = f.read()
for line in content:
     print(line)

# If you want print the line :--------------------------------------------

f = open("file.txt")
for line in f:
    print(line,end="") # used the end="" for remove space from the code.

#Readline function:--------------------------------------------------------------------------------------------------------------

f = open("file.txt")
print(f.readline()) # it is print the one line of the txt.
print(f.readline()) # it is print the second line of the txt.
print(f.readline()) # it is print the third line of the txt.
f.close()

# All line print in list function:--------------------------------------------------

f = open("file.txt")
print(f.readlines()) # it is print the list 
f.close()



