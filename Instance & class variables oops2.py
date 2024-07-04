# ---------------------------Instance & Class Variables OOPS In Python--------------------------------

class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4553
rohan.role = "Student"
print(rohan.name)
print(harry.role)

print(harry.no_of_leaves)
rohan.no_of_leaves = 9
print(rohan.no_of_leaves)

Employee.no_of_leaves = 9
print(Employee.no_of_leaves)

print(rohan.__dict__)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)
