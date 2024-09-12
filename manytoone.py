class student():
    def __init__(self,name,school):
        self.name=name
        self.school=school

class School:
    def __init__(self, name):
        self.name = name


school=School("WRC")
student1=student("Alice",school)
student2=student("Bob",school)

print(f"{student1.name} and {student2.name} attend {student1.school.name}")





