import sys
n = int(sys.stdin.readline())
list_n = [0] * 10001
for i in range(n):
    num = int(sys.stdin.readline())
    list_n[num] += 1

for i in range(10001):
    if list_n[i] != 0:
        for j in range(list_n[i]):
            print(i)
