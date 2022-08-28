import sys

n = int(sys.stdin.readline())

scores = []

for _ in range(n):
    score = int(sys.stdin.readline())
    scores.append(score)

result = [0 for _ in range(301)]

result[0] = scores[0]
if n >= 2:
    result[1] = scores[0] + scores[1]
if n >= 3:
    result[2] = max(scores[1] + scores[2], scores[0]+scores[2])

for i in range(3, n):
    result[i] = max(result[i-3] + scores[i-1] + scores[i], result[i-2] + scores[i])

print(result[n-1])