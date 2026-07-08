# write a function which contain one function chkGreater() that accepts two numbers and prints the greater number

def chkGreater():

    No1 = int(input("Enter first number : "))

    No2 = int(input("Enter second number : "))

    if No1 >= No2:
        large = No1
    else:
        large = No2

    print("The greater number is : ",large)


def main():

    chkGreater()

if __name__ == "__main__":
    main()
