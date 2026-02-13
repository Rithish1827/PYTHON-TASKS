def split(a):
    e,o = [],[]
    for i in a:
        (e if i%2==0 else o).append(i)
    print(e,o)

a = list(map(int,input().split()))
split(a)
