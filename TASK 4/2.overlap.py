def overlap(a, b):
    print("Common:", list(set(a)&set(b)))
    print("Either:", list(set(a)^set(b)))

a = input().split()
b = input().split()
overlap(a, b)
