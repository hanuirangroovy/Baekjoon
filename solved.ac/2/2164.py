from collections import deque
import sys

n = int(sys.stdin.readline())
list_n = deque()
for i in range(1, n+1):
    list_n.append(i)

while(len(list_n)>1):
    list_n.popleft()
    num = list_n.popleft()
    list_n.append(num)

print(list_n[0])