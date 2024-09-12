def show(a,n):
    if(a>n):
        return
    print(a)
    show(a+1,n)
n=int(input("enter the nth number"))
show(1,n)
