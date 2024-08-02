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

# Make a 3 class of Electronic device, Pocket gadget & Phone using of multilevel inheritence:-

class ElectronicsDevice:
    Ceilingfan = 12
    
class PocketGadget(ElectronicsDevice):

    Money =100
    Ceilingfan = 122

    def isMoney(self):
        return f"Yes I send the money{self.Money} of the company"
    
class Phone(PocketGadget):
    Money = 10

    # def isMoney(self):
    #     return f"Hello Yeah!"\
    #         f"Yes I need too much Money"

karan = ElectronicsDevice()
maran = PocketGadget()
saran = Phone()

print(saran.isMoney())

print(saran.Ceilingfan)