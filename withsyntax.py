with open("demo.txt","r") as f:
    data=f.read()
    print(data)

with open("demo.txt","w") as f:
    a=input("enter any line")
    f.write(a)