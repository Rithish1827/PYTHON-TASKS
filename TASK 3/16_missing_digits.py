n = input()
missing = []

for i in range(10):
    if str(i) not in n:
        missing.append(i)

print(missing)
