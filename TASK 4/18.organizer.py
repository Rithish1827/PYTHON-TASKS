def org(a):
    r = {}
    for i in a:
        e = i.split(".")[-1]
        r.setdefault(e, []).append(i)
    print(r)

a = eval(input())
org(a)
