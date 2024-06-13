# Args and Kwargs in python:-----


#Args In Python👇:-------------------------------------------------

def function_name_print(a,b,c,d,e):
    print(a,b,c,d,e)
    

def funargs(*args):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(args[4])
    print(args[5])
    print(type(args))


# function_name_print("Herry","Marry","Carry","Larry","Soman")    

har = ["Harry","Larry","Carry","Cheery","Dan","Bilzerian"]
funargs(*har)



def funargs(*args):
    for item in args:
        print(item)

har = ["Harry","Merry","Carry","Larry","Ronaldo","Dualipa"]
funargs(*har)




def funargs(normal, *args):
    print(normal)
    for item in args:
        print(item)
har = ["Harry","Merry","Carry","Larry","Ronaldo","Dualipa"]
normal = 34
funargs(normal, *har)


def function_name_print(a,b,c,d,e):
    print(a,b,c,d,e)
function_name_print("Harry","Rohan","Skillf","Hammad","Shivam")



def funargs(normal, *args):
    print(normal)
    for item in args:
        print(item)
    
har = ["Liila","Kamal","Sujan","Radhey","Bhole","Golla","The Programmer","Malad","Avantika"]
normal = 34
funargs(normal, *har)

# Kwargs In Python👇 :-------------------------------------------------------------------------------------

def funargs(normal, *argsrohan,**kwargs):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would like to introduce some of our heroes")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

har = ["harry","Rohan","Skillf","Hammad","Shivam"]
normal = "I am a normal Arguments and the students are:"
kw = {"Rohan":"Monitor","Harry":"Fitness Instructor","The programmer":"Coordinator","Shivam":"Ballyball Tranair"}
funargs(normal, *har,**kw)


def funargs(normal, *argsansh,**kwargs):
    print(normal)
    for item in argsansh:
        print(item)
        print("\nNow I would like to introduce some of our heroes")
        for key,value in kwargs.items():
            print(f"{key} is a {value}")

har = ["Harry","Rohan","SkillF","Hammd","Shigri","Laiba"]
normal = "I am a normal Arguments and the students are:"
kw = {"Rohan":"Monitor","Shubham":"Engineer","Arnald":"Gamer",
      "Kajuna":"Italian Popper"}
funargs(normal, *har,**kw)