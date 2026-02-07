n = int(input("Enter number: "))
lst = [x for x in range(1, n+1) if x % 3 == 0]
print("List of numbers divisible by 3:", lst)