def palindrome(No):

    if No < 0:
        return False

    rev = 0
    flag = No

    while No > 0:
    
        digit = No % 10

        rev = (rev * 10) + digit

        No = No // 10

    return flag == rev



def main():
    value = int(input("Enter a number : "))

    if palindrome(value):
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")


if __name__ == "__main__":
    main()