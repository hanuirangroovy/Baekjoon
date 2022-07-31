import sys

n = int(sys.stdin.readline())
list_n = sorted(list(map(int,sys.stdin.readline().split())))
m = int(sys.stdin.readline())
list_m = list(map(int,sys.stdin.readline().split()))

result = {}
for i in list_n:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
for i in list_m:
    if i in result:
        print(result[i], end= " ")
    else:
        print(0, end = " ")
