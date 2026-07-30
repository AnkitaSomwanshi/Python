class Demo:

    #class variables

    value1 = 10
    value2 = 20

    def __init__(self):
        self.No1 = 11
        self.No2 = 21

    #Instance Method

    def fun(self):
        print("Inside instance method named as fun")
        print(self.No1)
        print(self.No2)
        print(Demo.value1)
        print(Demo.value2)

dobj = Demo()
dobj.fun()