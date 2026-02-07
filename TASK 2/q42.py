w = float(input())
p = float(input())
amt = w*p
print(amt - amt*0.05 if w > 10 else amt)
