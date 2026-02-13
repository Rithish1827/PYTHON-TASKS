def merge(a,b):
    for k in a:
        a[k]+=b[k]
    print(a)

a=eval(input())
b=eval(input())
merge(a,b)
