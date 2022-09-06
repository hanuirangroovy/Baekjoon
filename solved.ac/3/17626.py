import sys

n = int(sys.stdin.readline())
list_n = [0]*(n+1)
list_n[0] = 0
list_n[1] = 1

for i in range(2, n+1):
    minV = 1e9
    num = 1
    while (num**2) <= i:
        minV = min(minV, list_n[i-(num**2)])
        num += 1
    list_n[i] = minV + 1

print(list_n[n])
