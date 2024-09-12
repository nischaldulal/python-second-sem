def fun1():
    try:
        l=[1,2,3,4,5]
        i=int(input("enter the index"))
        print(l[i])

    except:
        print("some error occurs")

    finally:
        print(("i am always executed"))   #why to use

    print("I am always executed")

x=fun1()
print(x)