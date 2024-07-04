# ----------------------------------Creating Our First Class In Python:------=----------------------

class student:
    pass
harry = student()
larry = student()
print(harry,larry)

harry.name = "Harry"
harry.std = 12
harry.section = 1
larry.std = 9
larry.subject = ["Hind","English","Physics"]
print(harry.name)
print(harry.std)
print(harry.section)
print(harry.std,larry.subject)
print(harry.name,larry.std)
