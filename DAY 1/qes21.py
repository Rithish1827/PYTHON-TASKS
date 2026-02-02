a = int(input())
b = int(input())
c = int(input())

if (a<=0 or b<=0 or c<=0):
    print("Enter valid Angle")
elif a+b+c == 180 :
    print("Valid Triangle")
else :
    print("Not a valid Triangle")