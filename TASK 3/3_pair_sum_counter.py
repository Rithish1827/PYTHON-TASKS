n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
k = int(input("Enter target sum: "))

count = 0
for i in range(n):
    for j in range(i+1, n):
        if lst[i] + lst[j] == k:
            count += 1

print(count)
