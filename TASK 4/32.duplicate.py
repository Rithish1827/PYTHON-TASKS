def dup(a):
    print(len(a)!=len(set(a)))

a=list(map(int,input().split()))
dup(a)
