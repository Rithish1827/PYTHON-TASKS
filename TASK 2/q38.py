s = int(input())
n = int(input())
for i in range(n):
    if s > 0:
        print("BOOKED")
        s -= 1
    else:
        print("HOUSEFULL")
        break
if s > 0:
    print(s)
