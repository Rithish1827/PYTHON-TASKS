a = int(input())
b = int(input())
c = int(input())

if a+b<c or b+c<a or c+a<b :
    print("Not a valid Triangle")
else :
    if a==b and b==c and c==a :
        print("Equilateral")
    elif a==b or b==c or c==a :
        print("Isosceles")
    elif a!=b and b!=c and c!=a :
        print("Scalene")