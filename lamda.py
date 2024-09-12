# def double(x):
#     return x*2

double=lambda x: x*2
print(double(5))

add = lambda *x:sum(x)

print(add(4,5,6))

# passing function
def appl(fx,value):
    return 6+fx(value)

print(appl(add,2))