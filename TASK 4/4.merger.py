def merge(a, b):
    for k in b:
        a[k] = a.get(k, 0) + b[k]
    print(a)

a = eval(input())
b = eval(input())
merge(a, b)
