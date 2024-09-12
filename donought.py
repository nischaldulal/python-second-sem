import matplotlib.pyplot as plt
x=[10,20,30,40]
x1=[40,30,20,10]
y=["C","c++","java","python"]
ex=[0.0,0.0,0.0,0.3]
plt.pie(x,labels=y,radius=1)
cr=plt.Circle(xy=(0,0),radius=0.5,facecolor="w")
plt.gca().add_artist(cr)

plt.show()