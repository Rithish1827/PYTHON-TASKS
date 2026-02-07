b = int(input())
if b < 10000: r = 3
elif b <= 50000: r = 5
else: r = 7
print((b*r/100)/12)
