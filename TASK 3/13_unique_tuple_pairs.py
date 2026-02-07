n = int(input())
lst = []

for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a, b))

res = []
for x in lst:
    if (x[1], x[0]) not in res:
        res.append(x)

print(res)
