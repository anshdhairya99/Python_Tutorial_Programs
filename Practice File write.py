# Practice File Write-------------------------------------

f =open("Ansh.txt","w")
f.write("Hello India\n")
f.close()


f=open("Ansh2.txt","w")
f.write("Hello England\n")
f.close()


f=open("Ansh2.txt","a")
f.write("Hey Petter\n")
f.close()


# Return value of how much the character are written it--------------------------------


f=open("Ansh2.txt","a")
a=f.write("Hello World\n")
print(a)
f.close()


# Open file read & Write------------------------------------

f=open("Ansh2.txt","r+")
print(f.read())
f.write("Thank you\n")
