def dt(a):
    r={}
    for i in a:
        if i["dept"] not in r or i["marks"]>r[i["dept"]]["marks"]:
            r[i["dept"]]=i
    print(r)

a=eval(input())
dt(a)
