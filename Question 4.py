# Write a function to accept two numbers and return their multiplication

def Multiplication(Value1, Value2):
    mult = Value1 * Value2
    return mult

def main():
    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    No2 = int(input())

    Ans = Multiplication(No1,No2)

    print("Multiplication of two numbers is  : ",Ans)

if __name__ == "__main__":
    main()

