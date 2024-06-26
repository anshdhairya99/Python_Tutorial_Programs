# Enumerate in Python:-----------------------------------------------------------------

list1 = ["Bhindi","Aloo","Chopsticks","chowmein"]

i  = 1
for item in list1:
    if i%2 is not 0:
        print(f"Jarvis please buy {item}")
    i += 1



# Best way to enumerate:---------------------------------------------------------------------

for index, item in enumerate(list1):
     if index%2==0:
         print(f"Jarvis please buy {item}")


list2 = ["Butterscotch","Vanilla","Pista","Matka Kulfi","Magnum"]

i = 1
for item in list2:
    if i%2 is not 0:
        print(f"Jarvis please buy {item}")
    i+=1


for index , item in enumerate(list2):
    if index%2==0:
        print(f"Jarvis please buy {item}")


