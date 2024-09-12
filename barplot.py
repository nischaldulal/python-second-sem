import matplotlib.pyplot as plt
import numpy as np
x=["Python","C","C++"]
y=[90,55,82]
z=[33,56,44]
p=np.arange(len(x))
width = 0.2
p1=[j+width for j in p ]

plt.xlabel("Language",fontsize=15)
plt.ylabel("Popularity",fontsize=15)
plt.title("Languages and populatrity",fontsize=30)

plt.bar(p,y,width,color="y",align="center",edgecolor="r",label="NISCHAL")
plt .bar(p1,z,width,color="g",align="center",edgecolor="r",label="NISCHAL1")

plt.xticks(p+width/2,x,rotation=10)
plt.legend()

plt.show()