def idx(a):
    r={}
    for i in a:
        r[i["name"]] = i["marks"]*0.7 + i["attendance"]*0.3
    print(r, max(r,key=r.get))

a=eval(input())
idx(a)
