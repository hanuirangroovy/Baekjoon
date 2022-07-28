import sys

n = int(sys.stdin.readline())
list_n = []
for i in range(n):
    list_n.append(int(sys.stdin.readline()))
list_n = sorted(list_n)

for i in list_n:
    sys.stdout.write(str(i)+'\n')
