# def average(a,b=3):
#     print("the average is",(a+b)/2)

# average(4,5)
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("average is:",sum/len(numbers))

def name(** name):
    print("hello",name["fname"])