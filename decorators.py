def hello():
    print("hello world")
 
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("thanks for using this function")
    return mfx
 
@greet
def hello():
    print("hello world")

hello()

@greet
def add(a, b):
    print(a + b)

add(4, 6)
