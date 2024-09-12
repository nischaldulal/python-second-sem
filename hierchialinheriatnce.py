class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Male(Human):
    def __init__(self, name, age, power):
    
        Human.__init__(self, name, age)
        self.power = power

    def info(self):
        print(f"Hey, I am {self.name} with age {self.age} and I have {self.power} power.")

class Female(Human):
    def __init__(self, name, age, power):
       
        Human.__init__(self, name, age)
        self.power = power

    def info(self):
        print(f"Hey, I am {self.name} with age {self.age} and I have {self.power} power.")


ram = Male("Ram", 32, "masculine")
anupa = Female("Anupa", 19, "cute")

# Calling methods
ram.info()
anupa.info()
