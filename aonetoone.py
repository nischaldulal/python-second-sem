class passport():
    def __init__(self,pno):
        self.pno=pno

class person():
    def __init__(self,name,passport ):
        self.name=name
        self.passport=passport

passportno=passport("126475")
person=person("Nischal",passportno)
print(f"{person.name} has passport number {person.passport.pno}")




# class tyre():
#     def __init__(self,tyre):
#         self.tyre=tyre

# class car():
#     def __init__(self,car,tyre):
#         self.car=car
#         self.tyre=tyre

#     def info(self):
#         print(f"{self.car} has {self.tyre} tyre")

# mrf=tyre("mrf")

# mustang=car("Mustang",mrf)
# mustang.info()

class Tyre:
    def __init__(self, tyre):
        self.tyre = tyre

class Car:
    def __init__(self, car, tyre):
        self.car = car
        self.tyre = tyre

    def info(self):
        print(f"{self.car} has {self.tyre.tyre} tyres")

mrf = Tyre("mrf")
mustang = Car("Mustang", mrf)
mustang.info()
