class book():
    def __init__(self,b,code):
        self.b=b
        self.code=code

class library():
    def __init__(self):
        self.books=[]

    def add_book(self,book):
        self.books.append(book)

 
 

book1=book("Nischal",987)
book2=book("Apple is good for health",028)

library=library()
library.add_book(book1)
library.add_book(book2)
print(f"Library has the books: {[book.b for book in library.books]}")





class student():
    def __init__(self,name):
        self.name=name

class school():
    def __init__(self):
        self.students=[]


    def addstudent(self,student):
        self.students.append(student)

student1=student("nischal")
student2=student("chirangibi")
student2=student("prabin")
school=school()

school.addstudent(student1)

school.addstudent(student2)

school.addstudent(student2)

x=[student.name for student in school.students]
print(x)

