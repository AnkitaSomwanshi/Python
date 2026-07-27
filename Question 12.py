# Write a program that accepts one number and check whether it is prime or not

def prime(No):
    if (No <= 1):
        return False

    for i in range(2,No):

        if No % i == 0:
            return False
        
    return True


def main():

    value = int(input("Enter a number : "))

    if prime(value):
        print("Number is prime")
    else:
        print("Number is not prime")

if __name__ == "__main__":
    main()