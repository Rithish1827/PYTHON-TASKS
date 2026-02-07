r = int(input())
c = int(input())
mat = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    mat.append(row)

for j in range(c):
    s = 0
    for i in range(r):
        s += mat[i][j]
    print(s)
