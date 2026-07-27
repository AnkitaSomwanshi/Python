# Write a lambda function using reduce() which accepts list of numbers and returns the maximum element

from functools import reduce 

Max = lambda x,y : x if x>y else y

def main():

    n = int(input("How many no of elements you want to enter in list : "))

    Data = []

    for i in range(n):
        element = int(input(f"Enter element {i+1} :"))
        Data.append(element)

    print("List Before reduce is : ",Data)

    rData = reduce(Max, Data)

    print("List after reduce : ",rData)

if __name__ == "__main__":
    main()