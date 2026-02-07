n = int(input())
c = 0
for i in range(1,n+1):
    t = i
    ok = True
    while t > 0:
        if t%10 == 4:
            ok = False
            break
        t //= 10
    if ok:
        c += 1
print(c)
