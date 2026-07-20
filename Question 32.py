# Write a lambda function using reduce() which accepts list of numbers and returns the addition of all elements

from functools import reduce 

addition = lambda x,y : x+y # x*y

def main():

    n = int(input("How many no of elements you want to enter in list : "))

    Data = []

    for i in range(n):
        element = int(input(f"Enter element {i+1} :"))
        Data.append(element)

    print("List Before reduce is : ",Data)

    rData = reduce(addition, Data)

    print("List after reduce : ",rData)

if __name__ == "__main__":
    main()