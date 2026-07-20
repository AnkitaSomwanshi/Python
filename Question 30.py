# write a lambda function using map() which accepts a list of numbers and returns a list of squares of each number

square = lambda x : x * x 


def main():

    n = int(input("How many elements do you want to enter? : "))

    Data = []

    # Loop to collect each element
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        Data.append(element)

    
    #Data = [5,8,9,10,12] 
    
    print("Data Before Map : ",Data)

    mData = list(map(square,Data))

    print("Data after Map : ",mData)

if __name__ == "__main__":
    main()