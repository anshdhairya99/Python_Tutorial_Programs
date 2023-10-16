# More On Files:----------------------------------------

#  :- tell()

f =open("Carry.txt")
print(f.tell()) # to know where is my *file-Pointer* used [tell()]--
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.close()

# seek() :--

f = open("Carry.txt")
print(f.readline())
f.seek(5) # it is skip the letter from the front of line.
print(f.readline())
f.seek(2)
print(f.readline())
f.close()

