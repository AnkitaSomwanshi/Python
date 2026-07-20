# Write a program which accepts one character and checks whether it is vowel or constants

def VowelCons(x):

    if(x=='A' or x=='a' or x=='E' or x=='e' or x=='I'
    or x=='i' or x=='O' or x=='o' or x=='U' or x=='u'):
        print("Its Vowel")
    else:
        print("its Consonant")



#    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

#    if len(x) == 1 and x.isalpha():
#        if x in vowels:
#            print(f"'{x}' is a Vowel.")
#        else:
#            print(f"'{x}' is a Consonant.")
#    else:
#        print("Invalid input.")

    
def main():

    c = input("Enter a character : ")

    VowelCons(c)

if __name__ == "__main__":
    main()