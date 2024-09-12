import matplotlib.pyplot as plt
import numpy as np
x=["Python","C","C++","Java"]
y=[85,70,60,82]
z=[20,44,34,66]
width=0.2
p=np.arange(len(x))
p1=[j+width for j in p]
plt.xlabel("languages")
plt.ylabel("No.")
plt.title("Nischal")
plt.barh(p,y,width,color="r",label="popularity")
plt.barh(p1,z,width,color="g",label="popularity1")
plt.xticks(p+width/2,x)
plt.legend()
plt.show()