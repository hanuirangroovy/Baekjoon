import sys

n = int(sys.stdin.readline())
lst_n = [0]*11
lst_n[1] = 1
lst_n[2] = 2
lst_n[3] = 4

for i in range(4,11):
    lst_n[i] = sum(lst_n[i-3:i])

for _ in range(n):
    num = int(sys.stdin.readline())
    print(lst_n[num])

