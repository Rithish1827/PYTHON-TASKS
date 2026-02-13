def library(a):
    r = {}
    for i in a:
        if i["days"] > 7:
            print(i["student"])
        r[i["book"]] = r.get(i["book"], 0) + 1
    print(r)

a = eval(input())
library(a)
