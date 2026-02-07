n=int(input())
m=int(input())
def is_prime(x):
    if x<2:
        return False
    for i in range(2 , int(x ** 0.5)+1):
        if x%i==0:
            return False
    return True
lst=[]
for i  in range(n,m+1):
    if is_prime(i):
        lst.append(i)
print(lst)