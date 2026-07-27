# Write a program which accept one number and print that many number from 1 to that number in reverse order

def numbers(value):

    my_range = range(1,value+1)

    for i in my_range:
        print(my_range[-i])



def main():

    num = int(input("Enter a number : "))

    numbers(num)


if __name__ == "__main__":
    main()