def maze(cr,cc,er,ec):
    rightway=0
    downway=0
    if (er==cr and ec==cc):
        return 1
    if (er==cr):
        rightway=maze(cr,cc+1,er,ec)
    if ec==cc:
        downway=maze(cr+1,cc,er,ec)

    if(cc<ec and cr<er):
        rightway=maze(cr,cc+1,er,ec)
        downway=maze(cr+1,cc,er,ec)
    return rightway+downway

a, b = map(int, input("Enter the number of rows and columns separated by space: ").split())
print("the number of ways are",maze(1,1,a,b))

