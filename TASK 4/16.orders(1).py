def order(a):
    r = {}
    for i in a:
        r[i] = r.get(i,0)+1
    print(max(r, key=r.get))
    print([k for k in r if r[k]==1])

a = eval(input())
order(a)
