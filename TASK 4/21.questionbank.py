def bank(d):
    u = set().union(*d.values())
    print(u)
    for k in d:
        if set(d[k]) == u:
            print(k)

d = eval(input())
bank(d)
