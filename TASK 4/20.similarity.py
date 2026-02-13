def sim(a,b):
    s = len(set(a)&set(b))/len(set(a)|set(b))
    print(s, s>=0.5)

a = input().split()
b = input().split()
sim(a,b)
