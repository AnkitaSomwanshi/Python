# Write a lambda function which accepts one number and returns True if number is even otherwise False

Even = lambda x : True if x % 2 == 0 else False

num = int(input("Enter a number : "))

Res = Even(num)

print(Res)