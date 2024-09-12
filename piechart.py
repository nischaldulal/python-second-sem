import matplotlib.pyplot as plt
x=[10,20,30,40]
y=["c","c++","java","python"]
c=["r","b","g","y"]
ex=[0.4,0.0,0.0,0.0]
plt.pie(x,radius=1,labels=y,explode=ex,
        colors=c,autopct="%0.2f%%",shadow=True,labeldistance=1,startangle=0,
        textprops={"fontsize":15},counterclock=False,
        wedgeprops={"linewidth":6,"edgecolor":"m"},rotatelabels=True)
plt.title("NISCHAL")
plt.legend(loc=2)
plt.show()