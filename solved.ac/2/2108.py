import sys
from collections import Counter


n = int(sys.stdin.readline())
list_n = []
for i in range(n):
    list_n.append(int(sys.stdin.readline()))
list_n.sort()
result = []

result_a = 0
for i in range(n):
    result_a += list_n[i]
result_a /= n
result.append(round(result_a))


result_b = list_n[int((n-1)/2)]
result.append(result_b)

cnt_c = Counter(list_n).most_common()
if len(list_n) >1 and cnt_c[0][1] == cnt_c[1][1]:
    result.append(cnt_c[1][0])
else:
    result.append(cnt_c[0][0])

result.append(list_n[-1] - list_n[0])


for i in range(4):
    print(result[i])
