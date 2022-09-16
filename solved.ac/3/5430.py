#https://www.acmicpc.net/board/view/25456
import sys
from collections import deque

tc = int(sys.stdin.readline())

for _ in range(tc):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    list_n = sys.stdin.readline().strip()[1:-1].split(',')
    queue = deque(list_n)

    cnt_D = p.count('D')
    cnt_R = 0

    if cnt_D >= n:
        print("error")
    else:
        for i in p:
            if i == 'R':
                cnt_R += 1
            elif i == 'D':
                if cnt_R % 2:
                    queue.pop()
                else:
                    queue.popleft()
        if cnt_R % 2:
            queue.reverse()
            print("[" + ','.join(queue) + "]")
        else:
            print("[" + ','.join(queue) + "]")

