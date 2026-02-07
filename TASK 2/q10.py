n = int(input())
t = n
r = 0
while t > 0:
    r = r*10 + t%10
    t //= 10
print("YES" if r == n else "NO")
