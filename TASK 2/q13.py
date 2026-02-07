n = int(input())
t = n
s = 0
while t > 0:
    d = t % 10
    f = 1
    for i in range(1,d+1):
        f *= i
    s += f
    t //= 10
print("STRONG" if s == n else "NOT STRONG")
