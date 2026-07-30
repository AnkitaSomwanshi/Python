from abc import ABC,abstractmethod   #(abstract Base class)

class Base(ABC):
    @abstractmethod
    def Addition(self,No1,No2):
        pass

class Derived(Base):
    pass


dobj = Derived()        #Error