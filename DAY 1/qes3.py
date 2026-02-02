p = int(input("Enter Pricipal:"))
r = float(input("Enter Rate:"))
t = int(input("Enter time period:"))

compound = (p*(1+r/100)**t)-p

print(compound)