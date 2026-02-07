n = int(input())
flat = []

for _ in range(n):
    sub = list(map(int, input().split()))
    for x in sub:
        flat.append(x)

print(flat)
