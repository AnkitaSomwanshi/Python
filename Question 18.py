# Write a program which accepts one number and print its factors
def factors(value):

    print("Factors are : ")
    for i in range(1,value+1):
        if value % i == 0:
            print(i)



def main():

    num = int(input("Enter a number : "))

    factors(num)


if __name__ == "__main__":
    main()