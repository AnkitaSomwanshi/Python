# write a program which accepts one number and prints sum of its digits

def Sum_digits(No):
    
    if No == 0:
        return 0
    
  
    sum = 0
    rem = 0
    while No > 0:
        rem = (No % 10) 
        print(rem)
        sum = sum + rem
        print(sum)
        No = No//10
        print(No)

    return sum


def main():
    value = int(input("Enter a number : "))

    print(f"Sum of digits is : {Sum_digits(value)}")

if __name__ =="__main__":
    main()