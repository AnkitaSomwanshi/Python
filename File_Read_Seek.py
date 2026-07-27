# seek(Kuthe, kuthun)

#0 starting
#1 current
#2 End

def main():
    try:
        fobj = open("Demo.txt","r")
        print("File gets opened")

        fobj.seek(10,0)             # skip till 10 character

        Data = fobj.read()

        print(Data)

    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()