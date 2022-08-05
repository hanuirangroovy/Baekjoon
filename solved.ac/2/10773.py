import sys

n = int(sys.stdin.readline())
sum = 0
lst_n = []
for i in range(n):
    num =  int(sys.stdin.readline())
    if num == 0:
        lst_n.pop()
    else:
        lst_n.append(num)
for i in range(len(lst_n)):
    sum += lst_n[i]
print(sum)