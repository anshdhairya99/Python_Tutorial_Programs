#*************************** PUBLIC , PRIVATE, & PROTECTED ACCESS SPECIFIC IN PYTHON******************************


# Public -  In which Everything have  read\write. used = used freely no sign
# Protected - Do not access other people and came in my child class. only subclasses have used other. used = _(Single underscore)
# Private - In a class employee only I used. Used - __(double underscore)

class Employee:
    var = 12
    _protec = 23
    __private = 234

emp = Employee("hello",23,"milido")
print(emp._Employee__private)


