n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

res = []
for x in lst:
    if lst.count(x) == 1:
        res.append(x)

print(res)
