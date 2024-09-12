class Duck:
    def swim(self):
        print("I am a duck and I can swim")
    def speaks(self):
        print("Quack Quack")

class Dog:
    def swim(self):
        print("I am a dog and i can swim")

    def speaks(self):
        print("woof woof")

def display(duck):
    duck.swim()
    duck.speaks()
    print("Information displayed")

d=Duck()
display(d)
print()
a=Dog()
display(a)
