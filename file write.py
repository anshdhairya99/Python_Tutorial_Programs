# File Write In Python:-------------------

f=open("HRX.txt","w")
f.write("HRX is the best brand\n")
f.close()

# Write the character ::----
f=open("HRX2.txt","w")
f.write("HRX is also a best brand\n")
f.close()

# Append the character :---
f=open("HRX2.txt","+a")
f.write("Hello HRX\n")
f.close()

# Return value of how much the character are written it:---------

f= open("HRX2.txt","a")
a = f.write("Hey HRX What are do that!")
print(a)
f.close()

# handle read and write both:--

f =open("HRX2.txt","r+")
print(f.read())
f.write("thank you\n")





