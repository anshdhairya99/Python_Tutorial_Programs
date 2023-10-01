# Simple String Program:-
"""mystr1 = "Hi Alexa"
mystr2 = "Hi Guru Randhawa"
print(mystr1)
print(mystr2)

#Indexing of the string :-
mystr = "HelloModi"
print(mystr[2])
# OR
mystr = "Stanford"
print(mystr[5])

# String Slicing:-
mystr = "Kamal Play the vallyball"
print("The length of the script is ",len(mystr))
print((mystr[0:25]))
#Advance Slicing :-

mystr = "Rohan is the very slim"
print("The length of",len(mystr))
print((mystr[0:5:2]))

#Advanced Slicing :-
mystr = "Hello Sam Altman"
print("The Legth of",len(mystr))
print(mystr[:5])
print(mystr[:])
print(mystr[::])
print(mystr[0:])
print(mystr[:5])
print(mystr[0:19:1])
print(mystr[::2])
print(mystr[0:23:1])
print(mystr[::2])
print(mystr[::-1])

# True/ False

mystr = "HelloAnkur"
print(mystr.isalnum())
print(mystr.isalpha())

# Used the multiple Strings in Python:-
mystr = "ANSH DHAIRYA"
print("This is length",len(mystr))
print(mystr.endswith("airya"))
print(mystr.endswith("bdoy"))
print(mystr.count("a"))
print(mystr.capitalize())
print(mystr.lower())
print(mystr.replace("the","are"))
print(mystr.find("NSH"))"""

#Strings Slicing:---

"""mystr = "Harry is the bad boy"
print(mystr) # came all print alphabets
print(len(mystr)) # print the length of alphabets
print(mystr[2]) # came the value r because it is on 2nd index
print(mystr[0:18]) #
print(mystr[0:20]) # carry all alphabets
print(mystr[0:5:2]) #it is skip the value 2 from fronts
print(mystr[:5]) # it cames the first letter of the value
print(mystr[5:]) # skip the first letter from the fronts
print(mystr[:])
print(mystr[::])
print(mystr[::2])
print(mystr[::3])
print(mystr[::12])"""

#Quick Revision:---

"""mystr1 = "Hello World I am Living in Dubai"
print(mystr1)
print(len(mystr1))
print(mystr1[3])
print(mystr1[0:3])
print(mystr1[0:33])
print(mystr1[0:20])
print(mystr1[0:5:2])
print(mystr1[5:])
print(mystr1[:])
print(mystr1[::])
print(mystr1[::2])
print(mystr1[::3])
print(mystr1[0::20])
print(mystr1[0:0:5])"""

#Negative Slicing:--

#mystr1 = "hello World I am Living in Dubai"
"""print(mystr1)
print(len(mystr1))
print(mystr1[-4:])
print(mystr1[-4:-2])
print(mystr1[-8:-5])
print(mystr1[-26:-20])
print(mystr1[::-1])
print(mystr1[::-2])
print(type(mystr1))
print(mystr1.isalpha())
print(mystr1.isalnum())
print(mystr1.endswith("Dubai"))
print(mystr1.count("a"))
print(mystr1.capitalize())
print(mystr1.find("am"))
print(mystr1.lower())
print(mystr1.upper())
print(mystr1.replace("am", "are"))"""

# Methods :-
# 1-Utility -

mystr1 = "hello world i am living in dubai"
print(mystr1.count("a")) 
print(mystr1.find("am"))
print(mystr1.replace("am", "are"))
print(mystr1.split()) # it is change in list
" ".join(mystr1)
print(mystr1.startswith("h"))
print(mystr1.endswith("dubai"))
print(mystr1.count("b"))
print(mystr1.upper())
print(mystr1.lower())
print(mystr1.title())
print(mystr1.find("dubai"))
print(mystr1.rfind("a"))
print(mystr1.index("dubai"))
print(mystr1.strip())
print(mystr1.capitalize())
print(mystr1.title())
print(mystr1.upper())
print(mystr1.lower())
print(mystr1.swapcase())
print(mystr1.casefold())
print(mystr1.isalnum()) # only including number
print(mystr1.isalpha()) # char and number.
print(mystr1.isdigit()) # (0-9) no only
print(mystr1.replace('a', 'am')) 
print(mystr1.split())
print(mystr1.find('am'))
print(' '.join(mystr1))
print(mystr1.strip())

