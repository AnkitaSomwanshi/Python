def Area(Radius, PI):
    Res = PI * Radius * Radius
    return Res

def main():
    Ret = Area(PI=3.14, Radius=5)
    print("Area of circle : ",Ret)

if __name__ == "__main__":
    main()
