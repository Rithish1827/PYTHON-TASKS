n=int(input())
t=n; s=0
while t>0:
    d=t%10
    s+=d**3
    t//=10
print("Armstrong" if s==n else "Not Armstrong")
