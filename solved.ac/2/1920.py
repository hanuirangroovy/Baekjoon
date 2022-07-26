def searchN(start, end, i):
    if start > end:
        return 0
    m = (start + end) // 2
    if list_n[m] == i:
        return 1
    elif list_n[m] > i:
        return searchN(start, m-1, i)
    else:
        return searchN(m+1, end, i)

n = int(input())
list_n = sorted(list(map(int, input().split())))
m = int(input())
list_m = list(map(int, input().split()))

for i in list_m:
    start = 0
    end = n-1
    print(searchN(start, end, i))



