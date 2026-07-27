# Write a program which accepts two numbers and print addition, substraction, multiplication and Division

def operations(num1, num2):

    Addition = (num1 + num2)
    print("Addition :",Addition)
    Subtraction = (num1 -num2)
    print("Subtraction : ",Subtraction)
    Multiplication = (num1 * num2)
    print("Multiplication :",Multiplication)
    Division = (num1 // num2)
    print("Division : ",Division)


def main():

    value1 = int(input("Enter first number : "))

    value2 = int(input("Enter second number : "))

    operations(value1, value2)


if __name__ == "__main__":
    main()