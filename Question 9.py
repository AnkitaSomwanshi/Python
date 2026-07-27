# write a program which accepts one number and print the square of that number

def square(value):

    res = value * value

    return res

def main():

    No1 = int(input("Enter a number : "))

    Ans = square(No1)

    print("A square of number is : ",Ans)

if __name__ == "__main__":
    main()