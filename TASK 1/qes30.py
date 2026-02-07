n=int(input())
p=1
while n>0:
    p*=n%10
    n//=10
print(p)
