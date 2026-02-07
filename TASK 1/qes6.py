l = int(input("Enter length: "))
b = int(input("Enter breadth: "))

area = l * b    
perimeter = 2 * (l + b)

print("Area =", area,"\nPerimeter =", perimeter, end="")

print("\n")

r =  float(input("Enter radius: "))

area_circle = 3.14 * r * r
circumference = 2 * 3.14 * r

print("Area of Circle =", area_circle, "\nCircumference =", circumference, end="")