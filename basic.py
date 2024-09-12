class Person:
    name="Nischal"
    occupation="ML engineer"
    salary="$100k"
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=Person()
a.info()