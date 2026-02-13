def allocation(a):
    s = set()
    for i in a:
        if i in s:
            print("Invalid:", i)
        s.add(i)

a = eval(input())
allocation(a)
