import matplotlib.pyplot as plt
x=[1,2,3,4,5]
area=[1,2,3,4,5]
area1=[2,3,2,6,0]
l=["area1","area2"]
plt.stackplot(x,area,area1,labels=l,baseline="wiggle")
plt.legend( )

plt.show()
