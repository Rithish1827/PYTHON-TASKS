n=int(input())
d=int(input())
c=0
while n>0:
    if n%10==d: c+=1
    n//=10
print(c)
