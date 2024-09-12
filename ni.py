a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
if((a>b) and (a>c)):
    print("the greatest is :",a)
elif((b>a) and (b>c)):
    print("the greatest is:",b)
else:
    print("the greatest is",c)