# Write a lambda function which accepts three numbers and returns largest number

largest = lambda x, y, z: x if (x>y and x>z) else (y if y>z else z)

num1 = int(input("Enter First number : "))

num2 = int(input("Enter Second number : "))

num3 = int(input("Enter Third number : "))

Res = largest(num1,num2,num3)

print("largest is : ",Res)