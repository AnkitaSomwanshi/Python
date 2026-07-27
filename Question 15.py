# Write a program which accepts one number and prints reverse of that number
def reverse(No):

    rev = 0 

    while No > 0:
    
        digit = No % 10

        rev = (rev * 10) + digit

        No = No // 10

    return rev



def main():
    value = int(input("Enter a number : "))

    print(f"Reverse number is : {reverse(value)}")

if __name__ == "__main__":
    main()