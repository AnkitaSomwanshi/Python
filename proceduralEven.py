def CheckEven(No):
    if (No % 2 == 0):
        print("Its Even Number")
    else:
        print("its Odd Number")
    
def main():
    value = int(input("Enter number : "))

    CheckEven(value)

if __name__ == "__main__":
    main()