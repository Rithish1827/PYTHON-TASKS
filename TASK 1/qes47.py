n=int(input())

s=sum(map(int,str(n)))

print("Harshad" if n%s==0 else "Not Harshad")
