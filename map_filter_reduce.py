def cube(x):
    return x*x*x
print(cube(2))
l=[1,2,3,4,5,6]
newl=[]
# for item in l:
#     newl.append(cube(item))
# print(newl)

# OR
newl=list(map(lambda x:x*x*x,l))
print(newl)

#filter
def filter_function(a):
    return a>4
n=list(filter(filter_function,l))
print(n)