from collections import deque
import sys

n = int(sys.stdin.readline())
deque = deque()
for i in range(n):
    deque_n = sys.stdin.readline().split()
    if deque_n[0] == 'push_front':
        deque.appendleft(deque_n[1])
    elif deque_n[0] == 'push_back':
        deque.append(deque_n[1])
    elif deque_n[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            deque.popleft()
    elif deque_n[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif deque_n[0] == 'size':
        print(len(deque))
    elif deque_n[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif deque_n[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif deque_n[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])