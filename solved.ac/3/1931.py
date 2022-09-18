import sys

n = int(sys.stdin.readline())

list_time = []

for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    list_time.append([start,end])

cnt = 0
last_time = 0

list_time = sorted(list_time, key=lambda x: (x[1],x[0]))

for start_time, end_time in list_time:
    if start_time >= last_time:
        cnt += 1

        last_time = end_time



print(cnt)