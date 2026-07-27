def CheckEven(No):
    return (No % 2 == 0)
       
    
def main():
    value = int(input("Enter number : "))

    Ret = CheckEven(value)

    if Ret == True:
        print("Its Even number")
    else:
        print("Its Odd number")

if __name__ == "__main__":
    main()