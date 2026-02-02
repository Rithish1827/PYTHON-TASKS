a = int(input())
notes = [500,200,100,50,20,10,1]
c = 0
for i in notes:
    c += a // i
    a %= i
print(c)
