# class Employee:
#     def __init__(self):
#         self.__name="harry"
# a=Employee()
# #print(a.__name) cant be acccessed directly
# print(a._Employee__name)#can be accesed indirectly "Name mangling"
# print(a.__dir__())

class student:
    def __init__(self):
        self._name="Harry"
    def _funname(self):# protected method
        return "CODE WITH HARRY"
    
class subject(student):     #inherited class
    pass

obj=student()
obj1=subject()

#calling by object of student class
print(obj._name)
print(obj._funname())

#callinf by object of subject class
print(obj1._name)
print(obj._funname())