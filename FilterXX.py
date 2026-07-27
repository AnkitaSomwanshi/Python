CheckEven = lambda No : (No % 2 == 0)

def main():
    Data = [13,24,26,29,34]
    print("Input Data is : ",Data)
    fData = list(filter(CheckEven, Data))
    print("Data after filter : ",fData)

if __name__ == "__main__":
    main()