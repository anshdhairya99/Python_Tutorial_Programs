# *******************************SINGLE INHERITENCE****************************************

class Employee:
    no_of_leaves = 8

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is{self.name}.Salary is{self.salary}.And Role is{self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-")) 
    @staticmethod
    def printgood(string):
        print("This is good"+ string)

class Programmer(Employee):
    def __init__(self, aname, asalary, arole,language):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = language



    def printprog(self):
        return f"The Programmer Name is {self.name}. Salary is {self.salary} and role is {self.role}.The language is{self.language}" 

# harry = Employee("harry", 255,"Instrctor")
# rohan = Employee("Rohan", 455, "Students")

Shubham = Programmer("Shubham", 444, "Hello",["python"])
karan = Programmer("Karan", 100000, "Engineer",["Python","C++"])
print(karan.printprog())
print(karan.printdetails())

