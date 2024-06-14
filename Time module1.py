# Time Module In Python:------------------------------

import time
initial = time.time()
k = 0
while(k<45):
    print("This is the good guy!")
    k+=1
    print("While loop ran in",time.time()-initial,"seconds")

initial2 = time.time()
for i in range(45):
    print("For Loop ran in",time.time-initial2())


import time
initial = time.time()
k = 0
while(k<45):
    print("Hello Mac Donalds can you make the recepie fast")
    time.sleep(2) #written the code within the gap of 2 seconds
    k+=1
    print("While loop ran in",time.time()-initial,"seconds")

initial2 = time.time()
for i in range(45):
    print("Hello Subway boys!")
    print("For Loop  ran in",time.time()-initial2,"seconds")

# To Calculate the time show the time present and year :--
# import time

localtime =time.asctime(time.localtime(time.time()))
print(localtime)