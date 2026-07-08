# write a program to display data type, memory address and size in bytes enter by the user
import sys

name = input("Enter your name : ")

print(name)
print(type(name))
print(id(name))
print(sys.getsizeof(name))