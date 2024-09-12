with open('myfile.txt','r') as f:
    print(type(f))
    #Move to the 10th byte in the file
    f.seek(20 )
    data=f.read(5)
    print(data)
    print(f.tell())