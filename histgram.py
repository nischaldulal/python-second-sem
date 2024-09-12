import matplotlib.pyplot as plt
import numpy as np
import random
def ramdom():
    x=np.random.randint(10,60,50)
    print(x)

def histogram():# oreintation ni hunxa horizontal r vertical
    no=[1,2,3,4,5,6,7,8,9,1,0,11,12,1,14,15,16,11,17,20,21,24,56,77,45,34,87,3,22,45,6,7,67,87,99,34]
    l=[0,20,40,60,80,100]
    plt.hist(no,color="g",log=True,rwidth=0.9,histtype="step",bins=l,bottom=20 ,edgecolor="r",cumulative=-1)
    plt.title("Nischal")
    plt.xlabel("python")
    plt.ylabel("No.")
    plt.axvline(40,color="r")
    plt.grid()
    plt.show()
histogram()
 