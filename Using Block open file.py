# Using Block To Open Files without using of file close(f.close()):---

with open("Ansh.txt") as f:
    a  = f.read(5)
    print(a)

with open("Ansh2.txt") as f:
    b = f.read(12)
    print(b)

with open("John.txt") as f:
    c = f.read(10)
    print(c)

with open("Carry.txt") as f:
    d = f.read(5)
    print(d)    

with open("file.txt") as f:
    e = f.read(8)
    print(e)    

with open("Carry.txt") as f:
    g =f.read(20)
    print(g)