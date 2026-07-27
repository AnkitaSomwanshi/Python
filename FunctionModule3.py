from Marvellous import Addition

def main():
    print("Enter First number: ")
    value1 = int(input())

    print("Enter second number: ")
    value2 = int(input())

    ret = Addition(value1,value2)                    

    print("Addition is : ",ret)

    ret = Substraction(value1,value2)   #Error

    print("Substraction is : ",ret)


if __name__ == "__main__":
    main()