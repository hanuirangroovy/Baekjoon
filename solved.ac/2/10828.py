import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    stack_n = sys.stdin.readline().split()
    if stack_n[0] == 'push':
        stack.append(stack_n[1])
    elif stack_n[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif stack_n[0] == 'size':
        print(len(stack))
    elif stack_n[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif stack_n[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
