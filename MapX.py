def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return No+1

def main():
    Data = [13,24,26,29,34]
    print("Input Data is : ",Data)
    fData = list(filter(CheckEven, Data))
    print("Data after filter : ",fData)
    mData = list(map(Increment,fData))
    print("Data after Map : ",mData)

if __name__ == "__main__":
    main()