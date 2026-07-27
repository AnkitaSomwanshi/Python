# Write a lambda function which accepts two numbers and returns maximum number

Max = lambda x,y: x if x>y else y

num1 = int(input("Enter First number : "))

num2 = int(input("Enter Second number : "))

Res = Max(num1,num2)

print("Max is : ",Res)