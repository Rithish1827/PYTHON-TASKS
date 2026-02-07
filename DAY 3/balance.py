balance = 0

while True:
    menu = input("Choose an option - Deposit (d), Withdraw (w), Check Balance (c), Exit (e): ").lower()
    if menu == 'd':
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Enter a positive amount.")
                continue
            balance += amount
            print(f"Deposited: {amount:.2f}. New balance: {balance:.2f}")
        except ValueError:
            print("Invalid amount. Please enter a number.")
    elif menu == 'w':
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Enter a positive amount.")
                continue
            if amount <= balance:
                balance -= amount
                print(f"Withdrew: {amount:.2f}. New balance: {balance:.2f}")
            else:
                print("Insufficient funds.")
        except ValueError:
            print("Invalid amount. Please enter a number.")
    elif menu == 'c':
        print(f"Current balance: {balance:.2f}")
    elif menu == 'e':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose d, w, c, or e.")