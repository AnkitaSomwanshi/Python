# Write a lambda function using filter() which accepts lists of elements and returns the count of even numbers

Even = lambda x : x % 2 == 0

def main():

    n = int(input("How many no of elements you want to enter in list : "))

    Data = []

    for i in range(n):
        element = int(input(f"Enter element {i+1} :"))
        Data.append(element)

    print("List Before filter is : ",Data)

    fData = list(filter(Even,Data))

    print("List after filter : ",fData)

    print("Count of even numbers: ",len(fData))

if __name__ == "__main__":
    main()