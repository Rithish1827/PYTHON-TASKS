def sensor(a):
    k = a[0].keys()
    for i in a:
        if i.keys() != k:
            print(i)

a = eval(input())
sensor(a)
