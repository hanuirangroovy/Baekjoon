import sys

def check_list():
    global result
    if len(list_s) == 1:
        if list_s[0] == "all":
            result = set([i for i in range(1, 21)])
        else:
            result = set()

    else:
        order, num = list_s[0], int(list_s[1])
        if order == "add":
            result.add(num)
        elif order == "remove":
            result.discard(num)
        elif order == "check":
            if num in result:
                print(1)
            else:
                print(0)
        elif order == "toggle":
            if num in result:
                result.discard(num)
            else:
                result.add(num)

n = int(sys.stdin.readline())
result = set()

for _ in range(n):
    list_s = sys.stdin.readline().strip().split()
    check_list()
