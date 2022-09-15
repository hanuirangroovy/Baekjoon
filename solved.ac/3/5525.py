import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline()

result = 0
cnt = 0
cnt_101 = 0

while cnt_101 < m-2:
    if s[cnt_101] == "I" and s[cnt_101+1] == "O" and s[cnt_101+2] == "I":
        cnt += 1
        cnt_101 += 1
        if cnt == n:
            cnt -= 1
            result += 1
    else:
        cnt = 0
    cnt_101 += 1
print(result)
