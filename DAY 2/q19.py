n = int(input())
r = 0
while n > 0:
    r = r*10 + n%10
    n //= 10
for i in range(2,r):
    if r%i == 0:
        print("NOT PRIME")
        break
else:
    print("PRIME")
