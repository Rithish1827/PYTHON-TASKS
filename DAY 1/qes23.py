a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

roots = (b**2)-(4*a*c)
if roots > 0 :
   print("Real and Distinct")
elif roots == 0 :
   print("Real and Equal")  
else :
   print("Imaginary")

print(roots)