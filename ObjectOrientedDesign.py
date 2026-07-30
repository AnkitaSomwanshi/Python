class Arithematic:

    #Instance method have first parameter as self

    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Addition(self):
        Ans = self.No1 + self.No2
        return Ans
    

    def Substraction(self):
        Ans = self.No1 - self.No2
        return Ans


print("Enter first number : ")
value1 = int(input())

print("Enter second number : ")
value2 = int(input())

Aobj = Arithematic(value1,value2)

#Ret = Addition(Aobj,value1,value2)
Ret = Aobj.Addition()         

print("Addition is : ",Ret)

Ret = Aobj.Substraction()

print("Substraction is : ",Ret)
