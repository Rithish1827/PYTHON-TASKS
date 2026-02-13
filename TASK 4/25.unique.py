def unique(m):
    for r in m:
        print(len(r)==len(set(r)))

m = eval(input())
unique(m)
