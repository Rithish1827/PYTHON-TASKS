def dept(a):
    r = {}
    for i in a:
        r.setdefault(i["dept"], []).append(i["cgpa"])
    for k in r:
        print(k, sum(r[k])/len(r[k]))

a = eval(input())
dept(a)
