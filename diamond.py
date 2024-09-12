class A:
    def display(self):
        print("display from A class")
class B(A):
    def display(self):
        print("display from B class")

class C(A):
    def display(self):
        print("display from c class")
    
    def show(self):
        print("hi from C class")


class D(B,C):
    pass

d1=D()
d1.display()
# print(D.mro())
        