# ---------------------------Self & __init__()(Constructor)_ Python------------------------------

# Self :--

# class Employee:
#     no_of_leaves = 8

#     def printdetails(self):
#         return f"The Name is {self.name}.Salary is {self.salary} and role is {self.role}"
     
# harry = Employee()
# rohan = Employee()

# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"

# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

# print(rohan.printdetails())
# print(harry.printdetails())

# print(rohan.no_of_leaves)


# ----------------------------------------Constructor:----------------------------------------------

class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is{self.name}.Salary is{self.salary} and role is{self.role}"
harry = Employee("Harry",255,"Instructor")

print(harry.salary)




