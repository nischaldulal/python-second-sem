from abc import ABC,abstractmethod

@abstractmethod
class Vehicle():
    def __init__(self,type):
        self.type=type
        pass
    @abstractmethod   
    def speed(self):
        pass

class car(Vehicle):
      def __init__(self,type,name,speed):
           super().__init__(type)
           self.name=name
    
      def speed(self):
           print("reuns at 50km/hr")


car1=car("car","mustang",144)
car1.speed()
     

        

