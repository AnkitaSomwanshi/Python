no =  11                            # Global Variable

def display():
    a = 21                          # Local variable
    print("From display : ",no)
    print("From display value of a is : ",a)
    pass

def demo():
    print("From demo : ",no)
    print("From demo value of a is : ",a)      #Error
    pass

display()

demo()  