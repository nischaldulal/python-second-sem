class hostelcard():
    def __init__(self, card_number):
        self.card_number =card_number 

class student():
    def __init__(self,name,cardnumber):
        self.name=name
        self.cardnumber=hostelcard(cardnumber)

student=student("Chirangibi Gautam ","12364358-A")
print(f"The student{student.name} reside inside the hostel of WRC has hostel cardnumber {student.cardnumber.card_number}")