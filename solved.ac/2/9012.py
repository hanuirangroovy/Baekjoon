import sys

n = int(sys.stdin.readline())

for i in range(n):
    ps = sys.stdin.readline()
    result = []
    answer = ''
    for j in ps:
        if j == '(':
            result.append(j)
        elif j == ')':
            if result:
                result.pop()
            else:
                answer = "NO"
                break
    else:
        if not result:
            answer = "YES"
        else:
            answer = "NO"
    print(answer)
