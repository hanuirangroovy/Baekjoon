import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    n = int(sys.stdin.readline())

    if n == 0:
        print(0)
        continue

    clothes = {}
    for _ in range(n):
        item, item_type = sys.stdin.readline().split()
        if item_type in clothes.keys():
            clothes[item_type] += 1
        else:
            clothes[item_type] = 2

        result = 1
        for key in clothes.keys():
            result *= clothes[key]

    print(result - 1)




