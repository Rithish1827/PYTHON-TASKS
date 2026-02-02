l = float(input())
p = float(input())
amt = int(l*p)
r = amt % 10
print(amt - r if r < 5 else amt + (10-r))
