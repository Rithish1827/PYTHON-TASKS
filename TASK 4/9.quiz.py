def quiz(d):
    r = {}
    for k in d:
        r[k] = sum(d[k])/len(d[k])
    c = sum(r.values())/len(r)
    print(r)
    print([k for k in r if r[k] > c])

d = eval(input())
quiz(d)
