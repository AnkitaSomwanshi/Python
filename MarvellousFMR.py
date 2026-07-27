from functools import reduce

CheckEven = lambda No : (No % 2 == 0)

Increment = lambda No : No+1

Addition = lambda No1,No2 : No1+No2

def filterX(Task,Elements):
    Result = []
    for no in Elements:
        ret = Task(no)  #CheckEven(no)
        if (ret == True):
            Result.append(no)

    return Result

def mapX(Task,Elements):
    Result = []
    for no in Elements:
        ret = Task(no)    #Increment(no)
        Result.append(ret)

    return Result
    
def reduceX(Task,Elements):
    sum = 0
    for no in Elements:
        sum = Task(sum,no)

    return sum

def main():
    Data = [13,24,26,29,34]
    print("Input Data is : ",Data)
    fData = list(filterX(CheckEven, Data))
    print("Data after filter : ",fData)
    mData = list(mapX(Increment,fData))
    print("Data after Map : ",mData)
    rData = reduceX(Addition,mData)
    print("Data after reduce : ",rData)

if __name__ == "__main__":
    main()