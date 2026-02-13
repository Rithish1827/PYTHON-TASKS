def resume(r, a):
    for i in a:
        m = len(set(i)&r)/len(r)
        if m >= 0.7:
            print(i)

r = set(input().split())
a = eval(input())
resume(r, a)
