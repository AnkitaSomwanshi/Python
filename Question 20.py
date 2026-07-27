# Write a program which accepts one number and print that many numbers starting from 1

def numbers(value):

    
    for i in range(1,value+1):
            print(i)



def main():

    num = int(input("Enter a number : "))

    numbers(num)


if __name__ == "__main__":
    main()