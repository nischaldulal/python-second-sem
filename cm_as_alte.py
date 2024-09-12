class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

e=Employee("harry",12000)
print(e.name)
print(e.salary)
print()


string="Harry-12000"
# e2=Employee(string.split("-")[0],string.split("-")[1])
e2=Employee.fromstr(string)
print(e2.name)
print(e2.salary)