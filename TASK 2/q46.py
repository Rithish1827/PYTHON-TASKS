pin = int(input())
ok = False
for i in range(3):
    if int(input()) == pin:
        ok = True
print("ACCESS GRANTED" if ok else "CARD BLOCKED")
