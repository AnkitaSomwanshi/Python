class Marvellous:
    No1 = 11                  #Class variable is part of class
    No2 = 12

    #In Oops if we want to create object we need to call __init__ method compulsory

    def __init__(self):       #Constructor call
        self.value1 = 21      #Instance variable is part of object
        self.value2 = 51

print(Marvellous.No1)
print(Marvellous.No2)

# Object / Instance Creation

mobj1 = Marvellous()
mobj2 = Marvellous()
mobj3 = Marvellous()

print(mobj1.value1)
print(mobj2.value1)