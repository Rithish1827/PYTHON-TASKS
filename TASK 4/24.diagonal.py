def diag(m):
    p=s=0
    n=len(m)
    for i in range(n):
        p+=m[i][i]
        s+=m[i][n-i-1]
    print(p,s)

m = eval(input())
diag(m)
