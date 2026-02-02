days = int(input("Enter days: "))

years = days // 365
weeks = (days % 365) // 7
days = (days % 365) % 7

print(years, "Years,", weeks, "Weeks and", days, "Days")
