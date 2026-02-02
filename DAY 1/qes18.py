units = int(input("Enter number of units consumed: "))

if units <= 100:
    bill = units * 1.5  
elif units <= 200:
    bill = (100 * 1.5) + (units - 100) * 2.0
elif units >= 300:
    bill = (100 * 1.5) + (100 * 2.0) + (units - 200) * 3.0

print(bill)