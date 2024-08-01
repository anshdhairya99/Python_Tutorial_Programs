# ************************MULTILEVEL INHERITENCE********************************************

class Dad:
    basketball = 1

class Son(Dad):
    dance =1 
    def isdance(self):
        return f"Yes I dance {self.dance} no of times"
    
class Grandson(Son):
    dance =6

# #     def isdance(self):
# #         return f"Jackson yeah!" \
# #             f"Yes I dance very awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()
print(harry.isdance())
print(harry.basketball)

# Make a 3 class of electronic device, pocket gadget & phone using of multilevel inheritence:-


