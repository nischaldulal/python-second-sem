from abc import ABC,abstractmethod
class Shape(ABC):

    def __init__(self,x,y):
        self.x=x
        self.y=y
        

    @property
    @abstractmethod
    def area(self):
        pass


class circle(Shape):

    def __init__(self,radius):
        super().__init__(radius,radius)

    @property
    def area(self):
        return 3.14*self.x*self.y
    

class Rectangele(Shape):
    
    @property
    def area(self):
        return self.x*self.y
    
y=Rectangele(4,6)
print(y.area)

     
    