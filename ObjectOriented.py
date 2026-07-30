class Arithematic:

    def Addition(No1,No2):
        Ans = No1 + No2
        return Ans
    
    # Ret = Addition(Aobj,value1,value2)

    def Substraction(No1,No2):
        Ans = No1 - No2
        return Ans

Aobj = Arithematic()

print("Enter first number : ")
value1 = int(input())

print("Enter second number : ")
value2 = int(input())

Ret = Aobj.Addition(value1,value2)          #Error

print("Addition is : ",Ret)

Ret = Aobj.Substraction(value1,value2)      #Error

print("Substraction is : ",Ret)
