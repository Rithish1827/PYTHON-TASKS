def pair(a):
    print([(i,i*i) for i in a])

a=list(map(int,input().split()))
pair(a)
