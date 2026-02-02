n = int(input("Enter a number: "))
sum = 0
for i in range(0, n + 1,2):
    sum+= i
print("Sum of even numbers from 1 to", n, "is:", sum) 