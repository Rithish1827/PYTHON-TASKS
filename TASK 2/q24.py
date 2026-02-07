h = int(input())
m = int(input())
x = int(input())
m += x
h += m // 60
m %= 60
h %= 24
print(h, m)
