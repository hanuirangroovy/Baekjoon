import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    list_n = [0, 1, 1, 1, 2, 2, 3]
    n = int(sys.stdin.readline())
    if n < 7:
        result = list_n[n]
    else:
        for i in range(6, n+1):
            list_n.append(list_n[i] + list_n[i-4])
        result = list_n[n]

    print(result)