b = int(input())
d = int(input())
h = 0
while b >= 20:
    b -= d
    h += 1
print(h if b < 20 else 0)
