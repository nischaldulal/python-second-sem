import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[2,3,4,5,3,2]
color=[45,76,88,60,47,34]
plt.title("Scatter Plot",fontsize=15)
plt.xlabel=("Days")
plt.ylabel=("No.")
plt.scatter(x,y,c=color,cmap="BrBG",s=100,marker="*",edgecolor="r")
t=plt.colorbar() 
t.set_label("color")
plt.show()