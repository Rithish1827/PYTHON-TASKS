def group(a):
    r={"<50":[], "50-74":[], ">=75":[]}
    for i in a:
        if i<50: r["<50"].append(i)
        elif i<75: r["50-74"].append(i)
        else: r[">=75"].append(i)
    print(r)

a=list(map(int,input().split()))
group(a)
