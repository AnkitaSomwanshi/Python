def Area(PI=3.14, Radius):                 #Error
    Res = PI * Radius * Radius
    return Res

def main():
    Ret = Area(5)
    print("Area of circle : ",Ret)

    Ret = Area(10.5, 7.12)
    print("Area of circle is : ",Ret)

if __name__ == "__main__":
    main()