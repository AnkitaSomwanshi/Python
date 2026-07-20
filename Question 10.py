# write a program that accept one number and print the cube of that number

def Cube(x):

    res = x * x * x

    return res

def main():

    No1 = int(input("Enter a number : "))

    Ans = Cube(No1)

    print("Cube of number is : ",Ans)

if __name__ == "__main__":
    main()
