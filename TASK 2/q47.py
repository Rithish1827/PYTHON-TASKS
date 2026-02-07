n = int(input())
for i in range(n):
    if int(input()) > 45:
        print("ALERT")
        break
else:
    print("SAFE")
