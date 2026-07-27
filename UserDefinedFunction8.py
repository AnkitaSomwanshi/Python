def BigBazar():
    print("Inside BigBazar")

    def Amul():
        print("Inside Amul Icecream Parlor")

def main():
    BigBazar()                # allowed
    Amul()                    # Error
    BigBazar.Amul()           # Error

   
    
if __name__ == "__main__":
    main()