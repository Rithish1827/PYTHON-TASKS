def vocab(a):
    s=set()
    for i in a:
        s|=set(i.split())
    print(s)

a=eval(input())
vocab(a)
