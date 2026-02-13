def wl(a):
    r={}
    for i in a:
        r.setdefault(len(i),[]).append(i)
    print(r)

a=input().split()
wl(a)
