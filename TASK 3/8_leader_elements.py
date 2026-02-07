lst = list(map(int, input().split()))
leaders = []
max_right = 0

for x in reversed(lst):
    if x > max_right:
        leaders.append(x)
        max_right = x

print(leaders[::-1])
