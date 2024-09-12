import numpy as np

def matrix():
    var=np.matrix([[1,2,3],[1,2,3]])
    var1=([[2,3,3],[2,5,6]])
    print(var)
    print(type(var))
    varm=np.multiply(var,var1)
    print(varm)
    

def array():
    var=np.array([[1,2,3],[1,2,3]])
    print(var*var)
    print(type(var))

matrix()
print()
array()