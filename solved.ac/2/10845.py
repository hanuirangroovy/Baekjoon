import sys

n = int(sys.stdin.readline())
queue = []
for i in range(n):
    queue_n = sys.stdin.readline().split()
    if queue_n[0] == 'push':
        queue.append(queue_n[1])
    elif queue_n[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif queue_n[0] == 'size':
        print(len(queue))
    elif queue_n[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif queue_n[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif queue_n[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])