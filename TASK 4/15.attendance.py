def attend(d, w):
    for k in d:
        print(k, len(d[k]))
        if d[k] == w:
            print("All days:", k)

d = eval(input())
w = set(input().split())
attend(d, w)
