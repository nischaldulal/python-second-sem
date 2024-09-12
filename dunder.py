class Employee:
    name="harry"

    def __init__(self,name):
        self.name=name
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    def __repr__(self):
        return (f"the name of the employee is { self.name}")

e=Employee("hari")
print(str(e))
print(repr(e))  