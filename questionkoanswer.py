with open("practice.txt","r") as f:
    data=f.read()
    
newdata=data.replace("Java","Python")
with open("practice.txt","w") as f:
    f.write(newdata)