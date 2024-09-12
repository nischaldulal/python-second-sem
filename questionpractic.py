# cities=["Tandi","Narayanghat","kathmandu","Pokhara","Nepalgunj"]
# name=["Nischal","Nischit","Biraj","Deep"]
# def leth(list):
#     print(len(list))
# def print_list(list):
#     for item in list:
#         print(item,end=" ")
# print_list(name)

def factorial(n):
    s=1
    for i in range(1,n+1,1):
        s*=i
    return s
n=int(input("enter the number"))
print("the factorial of the given number is",factorial(n))