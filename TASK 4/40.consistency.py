def con(a):
    k=a[0].keys()
    for i in a:
        if i.keys()!=k:
            print("Inconsistent")
            return
    print("Consistent")

a=eval(input())
con(a)
