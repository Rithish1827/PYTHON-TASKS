cp = int(input("Enter the cost Price:"))
sp = int(input("Enter the selling Price:"))

if cp > sp :
    print("Loss ")
elif sp > cp :
    print("Profit")
else :
    print("No Profit No Loss")