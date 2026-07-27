import Marvellous as MI   # Alias

def main():
    print("Enter First number: ")
    value1 = int(input())

    print("Enter second number: ")
    value2 = int(input())

    ret = MI.Addition(value1,value2)                    

    print("Addition is : ",ret)

if __name__ == "__main__":
    main()