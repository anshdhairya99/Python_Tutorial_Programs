# Enumerate in Python:-----

list1 = ["Bhindi","Aloo","Chopsticks","chowmein"]

i  = 1
for item in list1:
    if i%2 is not 0:
        print(f"Jarvis please buy {item}")
    i += 1