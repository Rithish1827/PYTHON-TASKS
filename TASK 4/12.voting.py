def vote(a):
    v = set()
    c = {}
    for i,j in a:
        if i in v:
            print("Invalid:", i)
        else:
            v.add(i)
            c[j] = c.get(j,0)+1
    print(c)

a = eval(input())
vote(a)
