r = int(input())
c = int(input())
mat = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    mat.append(row)

for row in mat:
    print(max(row))
