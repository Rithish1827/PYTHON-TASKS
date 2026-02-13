def clean(a):
    r = []
    for i in a:
        if i and i not in r:
            r.append(i)
    print(r)

a = eval(input())
clean(a)
