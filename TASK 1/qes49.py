n=int(input())
m1=m2=-1
while n>0:
    d=n%10
    if d>m1:
        m2=m1; m1=d
    elif d!=m1 and d>m2:
        m2=d
    n//=10
print(m2)
