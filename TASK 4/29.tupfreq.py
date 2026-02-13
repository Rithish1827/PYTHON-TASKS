def tf(a):
    r={}
    for i in a:
        r[i]=r.get(i,0)+1
    print(r)

a=eval(input())
tf(a)
