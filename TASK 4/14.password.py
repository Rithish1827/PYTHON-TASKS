def pwd(a):
    for i in a:
        if any(c.isdigit() for c in i) and any(not c.isalnum() for c in i):
            print("Valid:", i)
        else:
            print("Invalid:", i)

a = eval(input())
pwd(a)
