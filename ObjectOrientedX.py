class Arithematic:

    def Addition(Self, No1,No2):
        Ans = No1 + No2
        return Ans
    

    def Substraction(self, No1,No2):
        Ans = No1 - No2
        return Ans

Aobj = Arithematic()

print("Enter first number : ")
value1 = int(input())

print("Enter second number : ")
value2 = int(input())

#Ret = Addition(Aobj,value1,value2)
Ret = Aobj.Addition(value1,value2)         

print("Addition is : ",Ret)

Ret = Aobj.Substraction(value1,value2)      
print("Substraction is : ",Ret)
