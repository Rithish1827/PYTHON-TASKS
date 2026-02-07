n = int(input())
names = []
marks = []

for _ in range(n):
    names.append(input())
    marks.append(int(input()))

students = list(zip(names, marks))
students.sort(key=lambda x: -x[1])

rank = 1
for s in students:
    print(s[0], rank)
    rank += 1
