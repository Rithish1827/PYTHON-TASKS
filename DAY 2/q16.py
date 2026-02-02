n = int(input())
s = p = 0
p = 1
t = n
while t > 0:
    d = t % 10
    s += d
    p *= d
    t //= 10
print("VALID" if s%2==0 and p%3==0 else "INVALID")
