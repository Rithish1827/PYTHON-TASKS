def topk(a,k):
    r={}
    for i in a:
        r[i]=r.get(i,0)+1
    print(sorted(r,key=r.get,reverse=True)[:k])

a=list(map(int,input().split()))
k=int(input())
topk(a,k)
