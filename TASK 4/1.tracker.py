def tracker(d):
    m = 0
    t = ""
    for k in d:
        c = len(d[k])
        print(k, c)
        if c > m:
            m = c
            t = k
    print("Topper:", t)

d = eval(input())
tracker(d)
