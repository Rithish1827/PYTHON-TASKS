n=int(input())
e=o=0
while n>0:
    if (n%10)%2==0: e+=1
    else: o+=1
    n//=10
print(e, o)
