
# ADVANCE SLICING IN PYTHON :-------------------------------------


# In python indexing start with 0.
mystr = "Kamal play chess"
# Used length to find the length of mystr= "kamal play cricket"
print("The length of",len(mystr))
# In below 0 is the including and 19 is the excluding-
# When my length is 18 then we increase the 1 no as like as 18 to 19-
# also write the 18 there is no probleum.
# But not write the 17.
print(mystr[0:16])
print((mystr[0:100]))

#skiping the character -
mystr = "Harry is cute"
print("This is length",len(mystr))
print((mystr[0:5:2]))

mystr = "harry is a good boy"
print(len(mystr))
print(mystr[::9484788])
print(mystr[:])
print(mystr[::])
print(mystr[0:])
print(mystr[:5])
print(mystr[0:19:1])
print(mystr[::2])

#NEGATIVE INDEXING:-------------------

mystr = "hello the Moongchilla"
print(len(mystr))
print(mystr[-1:0])
print(mystr[-4:])
print(mystr[-4:-2])
#opposite the code:---------
print(mystr[::-1])



# consider false because upper hello moonchilla have a space if there is no space then
# true
print(mystr.isalnum())
print(mystr.isalpha())

 
# Multiple of functions and strings:--------------------
print(mystr.endswith("chilla"))
print(mystr.endswith("bdoy"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.find("ch")) # to find the no in which the no of position
print(mystr.lower())
print(mystr.replace("the","are")) # Used the new string.