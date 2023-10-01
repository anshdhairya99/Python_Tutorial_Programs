# Dictionary is nothing but key value pairs-------

#d1 = {}
#print(type())
d2 = {"Harry":"Burger",
      "Rohan":"Fish",
      "SkillF":"Roti",
      "Shubham":{"B":"maggie","L":"roti","D":"Chicken","A":"Mutton"}}
#print([d2])

# Used the capital name of:- And everyone have dictionary are in below.....
"""print(d2["Shubham"])
print(d2["Shubham"]["B"])
print(d2["Shubham"]["L"])
print(d2["Shubham"]["D"])
print(d2["Shubham"]["A"])"""

# find the Dictionary of every person:-------------------------------------
"""print(d2["Rohan"])
print(d2["Harry"]) 
print(d2["SkillF"])"""

# Add the string in d2 and you also add the number----------------------------------
"""d2["Ankit"] = "Junk Food"
d2["Anas"] = "Seak kabab"
d2[776]  = " Egg Roll"
d2["567"]  = "234"
d2["456"]  = "233" """

# when you want to delete the any function:-----------------------------
#del d2[776]
#print(d2)

#Dictionary Function you want that copy function---------------
#d3 = d2.copy()
"""d3 = d2
del d3["Harry"]
print(d2)
print(d2.get("Harry"))"""

# Update the function--------------------------
d2.update({"Leena":"Toffee"})
print(d2)

# Print all the keys------------------
#print(d2.keys())

#print all the key items----------------------------------
#print(d2.items())
