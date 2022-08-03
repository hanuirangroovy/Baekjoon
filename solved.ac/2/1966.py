import sys
tc = int(sys.stdin.readline())
for i in range(tc):
    n, m = map(int,sys.stdin.readline().split())
    list_n = list(map(int, sys.stdin.readline().split()))
    list_t = [False] * n
    list_t[m] = True
    cnt = 0
    while list_n:
        if list_n[0] == max(list_n):
            cnt += 1
            if list_t[0] == True:
                print(cnt)
                break
            list_n.pop(0)
            list_t.pop(0)
        else:
            list_n.append(list_n.pop(0))
            list_t.append(list_t.pop(0))
