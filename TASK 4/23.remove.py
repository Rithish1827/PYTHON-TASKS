def remove(a,b):
    print([i for i in a if i not in b])

a = list(map(int,input().split()))
b = list(map(int,input().split()))
remove(a,b)
