age = int(input())
price = 200
if age < 5:
    print(0)
elif age <= 12:
    print(price//2)
elif age >= 60:
    print(price - price*30//100)
else:
    print(price)
