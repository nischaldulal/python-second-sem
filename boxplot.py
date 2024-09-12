import matplotlib.pyplot as plt
x=[10,20,30,40,50,60,200]
y=[22,34,23,23,55,64,99]
z=[x,y]
plt.boxplot(z,notch=False,vert=True,
patch_artist=True,showmeans=True,
whis=1.5,sym="g+",boxprops=dict(color="r"),capprops=dict(color="r"),
whiskerprops=dict(color="r"),flierprops=dict(markeredgecolor="y"))
plt.show()