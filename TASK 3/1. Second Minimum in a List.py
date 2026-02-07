n = int(input("Enter number of elements: "))
lst = []
for _ in range(n):
    lst.append(int(input()))

m1 = m2 = float('inf')
for x in lst:
    if x < m1:
        m2 = m1
        m1 = x
    elif m1 < x < m2:
        m2 = x

print("Second minimum:", m2)
