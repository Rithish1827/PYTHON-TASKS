n = int(input())
s = 0
t = n
while t > 0:
    s += t % 10
    t //= 10
print("VALID" if s % 3 == 0 and n % 10 % 2 == 0 else "INVALID")
