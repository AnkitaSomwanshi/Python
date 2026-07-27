print("Enter your marks..")
marks = int(input())

if(marks>=40) and (marks<=50):
    print("you are in 3rd class")
elif(marks>50) and (marks<=60):
    print("you are in 2nd class")
elif(marks>60) and (marks<=70):
    print("you are in 1st class")
elif(marks>70) and (marks<=100):
    print("you are in distinction..")
elif(marks>100):
    print("Invalid")
else:
    print("you are fail")