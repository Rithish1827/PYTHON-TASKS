n = input()
s = sum(map(int,n))
print("ACCESS GRANTED" if len(n)==4 and s>15 else "ACCESS DENIED")
