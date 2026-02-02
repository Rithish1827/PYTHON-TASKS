b = int(input())
w = int(input())
if w % 100 == 0 and w <= b and b - w >= 500:
    print("SUCCESS")
else:
    print("REJECTED")
