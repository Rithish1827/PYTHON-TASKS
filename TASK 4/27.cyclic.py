def cyclic(a,b):
    print(len(a)==len(b) and b in a+a)

a=list(map(int,input().split()))
b=list(map(int,input().split()))
cyclic(a,b)
