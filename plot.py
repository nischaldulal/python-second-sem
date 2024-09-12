import matplotlib.pyplot as plt
import numpy as np
import math as s

x=np.linspace(-2*s.pi,2*s.pi,100)
y=np.sin(x)
plt.plot(x,y)
plt.fill_between(x,y,color="r",where=(y>0)&(y<=1))
plt.show()