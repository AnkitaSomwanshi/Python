# Write a program which accepts one number and prints count of digits in that number

def Count_digits(No):
    
    if No == 0:
        return 1
    
    count = 0
    while No > 0:
        No = No//10
        print(No)
        count = count + 1
        print(count)

    return count


def main():
    value = int(input("Enter a number : "))

    print(f"Count of digits is : {Count_digits(value)}")

if __name__ =="__main__":
    main()