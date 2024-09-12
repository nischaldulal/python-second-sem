a= input("enter the number")
try:
    print("the 10 times less than the number you provided is",10/int(a))
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
