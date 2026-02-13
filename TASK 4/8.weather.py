def weather(a):
    avg = [sum(i)/len(i) for i in a]
    print(avg, max(max(i) for i in a), avg.index(max(avg))+1)

a = eval(input())
weather(a)
