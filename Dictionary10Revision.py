#Dictionary is nothing but key value pairs :------------------
#If you want rhe null value :-----------------
#d1 = {}
#print(d1)
"""d2 = {"Ansh":"Apple",
      "Anoo":"Gobhi",
      "Shreya":"Chocho",
      "Mummy":"paneer",
      "Rohan":"Cake Lava",
      "Ajay":"Bhindi",
      "Vikrant":"chicken",
      "Kamlesh":{"A":"Murga","B":"Tikka","C":"Aloo"}}
#print(d2)"""
#used the capital no. of and eveyone have dictionary are in below
# find the dictionary of every person
"""print(d2["Ansh"])
print(d2["Anoo"])
print(d2["Shreya"])
print(d2["Mummy"])
print(d2["Rohan"])
print(d2["Ajay"])
print(d2["Vikrant"])
print(d2["Kamlesh"])
print(d2["Kamlesh"]["A"])
print(d2["Kamlesh"]["B"])
print(d2["Kamlesh"]["C"])
print(d2)
#Add the string in d2 and you also add the number------------
d2["Anas"] = "Junk Food"
d2["Chiku"] = "Lollypop"
d2["Raghav"] = "Frooty"
d2["Sona"] = "Pizza"
d2["Ankur"] = "Moongchilla"
d2[776] = "Egg Roll"
print(d2)
#When you want to delete any function ---------------------------------
del d2[776]
print(d2)"""
#Dictionary function you want that (copy) function----------------
#d3 = d2.copy()
#print (d2)
# To (delete) the function
"""d3 = d2
del d3["Ansh"]
print(d2)"""

#To (get) the item of specific name------
#print(d2.get("Ansh"))
#print(d2)
# In which to (update) the function in d2----------------------
"""d2.update({"Leena":"Tofee"})
print(d2)"""

#Print all the (keys)-------------------
"""print(d2.keys())
print(d2)"""

#Print all the key (items)------------------
"""print(d2.items())
print(d2)"""

# We used this newly operation-----------------------------------
""" Remove "model" From the Dictionary"""
#Used the (pop) operation in below------------
bike = {
 "brand":"Royal Enfield",
 "model":"Hunter 350",
 "year":"1960"
}
bike.pop("brand")
print(bike)

#Used the (popitem)------------
Car = {
"brand" : "Bugati",
"model" : "Chiron",
"year" : "1930"
}
Car.popitem()
print(Car)

# Used the (clear) dic-
fan = {
      "brand": "havells",
      "model": "Bt-07",
      "year" :  "1905"
}
fan.clear()
print(fan)

#Used the (Copy) dic---

shoes ={
"brand":      "Puma",
"model":      "Sneaker",
"estblished": "1901"
}
shoes.copy()
print(shoes)

# used the (fromkeys) dic--
x = ('keys1','keys2','keys3','keys4','keys5','keys6','keys7','keys8','keys9','keys10')
y = 0
thisdict = dict.fromkeys(x,y)
print(thisdict)

#Used the (get) in dic--

car ={
      "model" : "Urus",
      "brand" : "Lamborgini",
      "year": "1890"
}
x = car.get("brand")
print(x)

#Used the (items) in dict-----
cloth= {
      "Splash":"Tshirt",
      "Kappa":"Jacket",
"zudio":"Shoes"
}
x = cloth.items()
print(x)
# Used the (popiitems) in dic ----
car ={
      "model" : "Urus",
      "brand" : "Lamborgini",
      "year": "1890"
}
x = car.popitem()
print(car)
# Used the when any (setdefault)--
car ={
      "model" : "Urus",
      "brand" : "Lamborgini",
      "year": "1890"
}
x = car.setdefault("brand","Ansh")
print(x)
# In which we want to (update)-----------
car ={
      "model" : "Urus",
      "brand" : "Lamborgini",
      "year": "1890"
}
car.update({"colour":"black"})
print(car)
#If you want that (value) -----
car ={
      "model" : "Urus",
      "brand" : "Lamborgini",
      "year"  : "1890"
}
x = car.values()
print(x)


"""Question - To create a dictionary and taken from the user and return the  meaning of the word 
from  the dictionary."""


"""Solution of the above question"""

"""d3 = {"SET":"https://byjus.com/maths/what-is-a-set/",
      "TABLE":"A TABLE IS THE THERE ARE MANY NUMBERS ARE IN THE TABLE",
      "VARIABLE":"A VARIABLE IS THE COLLECTION OF CHARACTER",
      "ALPHABET":"A ALPHABET IS THE COLLECTION OF THE ALPHABETS",
      "MOUSE":"MOUSE IS THE HARDWARE IN WHICH WE MOVE THE CURSOR AROUND THE SCREEN AND  FIND ITS SOLUTION"
}
print('Enter Any Word For Meaning')
type = input()
print(d3[type])"""

#Dictionary :--

#d1 = {}
#print(type(d1))
"""d2 = {"Anmol":"Burger",
      "Suraj":"seek kebab",
      "Rahul":"Aloo matr",
      "sant":"chai","Shubham":{"B":"Chai And Roti","L":"Dal Chaval","D":"Sabji"}}"""
"""print(d2)
print(type(d2))
print(d2["Shubham"])
print(d2["Shubham"]["B"])
print(d2["Shubham"]["L"])
print(d2["Shubham"]["D"])
d2["Anand Mahindra"] = "Thar"
d2["Sahrukh Khan"] = "Gauri Khan"
del d2["Anand Mahindra"]
del d2["Sahrukh Khan"]
#print(d2["Anmol"])
#print(d2["Suraj"]) # it is case senstive
#d2["Joshi"] = "Riya"
print(d2)"""
#d3 = d2
#del d3["Anmol"]
#print(d2.get("Anmol"))
#print(d2.update({"lenna":"Tofe"}))
#print(d2.keys())
#print(d2.items())

"""x = {
    "Company": "TATA",
    "Brand": "NEXON",
    "Global NCAP": "5✨",
    "Model No.": "Er45"
}
print(x)
print(type(x))
a = x.popitem()
print(a)"""

"""d3 = {
    "Company": "TATA",
    "Brand": "NEXON",
    "Global NCAP": "5",
    "Model No.": "Er45"
}
d3.copy()
print(d3)"""

d4 = {"Harry":"Atal","Ansh":"lolypop","Anoo":"Chips"}
print(d4)
x = d4.items()
print(x)