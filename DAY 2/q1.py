n = input()
mid = len(n)//2
s1 = s2 = 0
for i in range(mid):
    s1 += int(n[i])
    s2 += int(n[i+mid])
print("BALANCED" if s1 == s2 else "NOT BALANCED")
