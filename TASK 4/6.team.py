def team(d):
    all_s = set()
    com = None
    for k in d:
        if "Python" in d[k] and "SQL" in d[k]:
            print(k)
        all_s |= d[k]
        com = d[k] if com is None else com & d[k]
    print(all_s, com)

d = eval(input())
team(d)
