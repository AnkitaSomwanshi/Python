# Write a lambda function using filter() which accepts list of numbers and returns the list of elements divisible by 3 and 5

from functools import reduce 

Division = lambda x : x % 3==0 and x % 5==0

def main():

    n = int(input("How many no of elements you want to enter in list : "))

    Data = []

    for i in range(n):
        element = int(input(f"Enter element {i+1} :"))
        Data.append(element)

    print("List Before reduce is : ",Data)

    fData = list(filter(Division, Data))

    print("List after reduce : ",fData)

if __name__ == "__main__":
    main()