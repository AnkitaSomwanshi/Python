# Write a function that accept one number and check wether that number is divisible by 3 and 5

def main():

    No1 = int(input("Enter a number : "))

    if (No1 % 3 ==0) and (No1 % 5 ==0 ):
        print("Number is divisible by 3 & 5")
    else:
        print("Number is not divisible by 3 & 5")


if __name__ == "__main__":
    main()