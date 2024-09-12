def stair(n):
    if n==0 : return 0
    if n==1: return n
    if n==2 : return n
    return stair(n-1)+stair(n-2)

print(stair(5))