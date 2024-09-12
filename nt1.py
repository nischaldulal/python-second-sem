def decreasing(n):
    if n==1: return
    print(n)
    decreasing(n-1)

decreasing(6)