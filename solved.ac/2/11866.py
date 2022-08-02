import sys
n, k = map(int,sys.stdin.readline().split())
lst_f = [False] * n
result = []
cnt = 0
num = k-1
while lst_f != [True]*n:
    num %= n
    if lst_f[k-1] == False:
        lst_f[num] = True
        result.append(num+1)
        num += 1
        cnt += 1
    elif lst_f[num] == False and cnt == k:
        lst_f[num] = True
        result.append(num+1)
        cnt = 1
        num += 1

    elif lst_f[num] == False:
        cnt += 1
        num += 1

    else:
        num += 1
print("<",end="")
for i in range(len(result)-1):
    print(result[i],end=", ")
print(result[-1],end="")
print(">",end="")