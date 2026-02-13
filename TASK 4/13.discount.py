def discount(d):
    for k in d:
        if d[k] > 10000:
            d[k] *= 0.8
        elif d[k] > 5000:
            d[k] *= 0.9
    print(d)

d = eval(input())
discount(d)
