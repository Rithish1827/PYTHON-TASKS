balance = int(input("Enter balance:"))
withdarwal = int(input("Enter withdrawal:"))

if withdarwal % 100 != 0:
    print("Withdrawal amount must be in multiples of 100")
else :
    if withdarwal<=balance and balance-withdarwal>=500:
        print("Withdrawal Successful")
    else :
        print("Withdrawal amount exceeds the balance/Minimum balance")

