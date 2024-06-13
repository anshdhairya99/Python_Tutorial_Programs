# Time Module In Python:------------------------------

import time
initial = time.time()
k = 0
while(k<45):
    print("This is harry bhai")
    k+=1
    print("While loop ran in",time.time()-initial,"Second")

initial2 = time.time()
for i in range(45):
    print("This is harry bhai")

print("For Loop ran in",time.time()-initial2,"seconds")