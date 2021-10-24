t = int(input())
for _ in range(t):
    k = int(input()) #층
    n = int(input()) #호
    lst = [i for i in range(1,n+1)]
    for x in range(k):
        for y in range(1,n):
            lst[y] += lst[y-1]

    print(lst[-1])