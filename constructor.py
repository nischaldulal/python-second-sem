class Person:
    def __init__(self,n,o):
        print("hey i am person")
        self.name=n
        self.occ=o
    def info(self):
        print(f"{self.name} is a {self.occ}")
a=Person("Nischal","ML engineer")
b=Person("Divya","Hr")
a.info()
b.info()
