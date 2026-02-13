def inv(d):
    r={}
    for k,v in d.items():
        r.setdefault(v,[]).append(k)
    print(r)

d=eval(input())
inv(d)
