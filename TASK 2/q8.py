n = int(input())
m = int(input())
for i in range(n-1):
    x = int(input())
    if x < m:
        m = x
print(m)
