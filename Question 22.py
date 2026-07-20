# Write a program which accepts one number and check whether it is perfect number or not

def perfect(value):

    sum = 0
    
    for i in range(1,(value//2)+1):
        if value % i == 0:
            sum = sum + i
    if value == sum:
        print("Its perfect number")
    else:
        print("Its not perfect number")

            
def main():

    num = int(input("Enter a number : "))
    
    perfect(num)

if __name__ == "__main__":
    main()
