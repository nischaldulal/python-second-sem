def fun(a,n):
    if a>=n:
        return
    print(a)
    fun(a+1,n)

fun(1,100)