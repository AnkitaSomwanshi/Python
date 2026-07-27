# Write a program which accepts one number and prints binary equivalent

def Binary(value):

    print(f"{value:04b}")

            
def main():

    num = int(input("Enter a number : "))
    
    Binary(num)

if __name__ == "__main__":
    main()