n=int(input("Enter a number: "))
lst = []
for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    lst.append((name, marks))
lst.sort(key=lambda x: x[1], reverse=True)
print(lst[0]) 