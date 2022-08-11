import sys

n = int(sys.stdin.readline())
list_n = []
result = []
cnt = 1
ans = True
for _ in range(n):
    num = int(sys.stdin.readline())
    while cnt <= num:
        list_n.append(cnt)
        result.append('+')
        cnt += 1
    if list_n[-1] == num:
        list_n.pop()
        result.append('-')
    else:
        ans = False

if ans == True:
    for i in result:
        print(i)
else:
    print('NO')