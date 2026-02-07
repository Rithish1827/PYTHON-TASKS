a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a + b  > a*b :
    print("Sum is greater")
elif a + b < a*b :
    print("Product is greater")
else :
    print("Both are equal")