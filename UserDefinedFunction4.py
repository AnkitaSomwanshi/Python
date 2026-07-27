# Accept:  multipal parameters
# Return:  1 value

def Marvellous(Value1, value2):
    print("Inside Marvellous : ",Value1, value2)
    return 21

def main():
    Ret = Marvellous(10, 20)
    print("Return value is : ",Ret)

if __name__ == "__main__":
    main()