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

    @classmethod
    def gun(cls):
        print("Inside class method named as gun")
        #print(Demo.No1)
        #print(Demo.No2)                    # Instance variable is not allowed in class method
        print(Demo.value1)
        print(Demo.value2)


# call with object

dobj = Demo()
dobj.gun()          #there is no need of  instance of class