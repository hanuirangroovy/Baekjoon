import sys

formula = sys.stdin.readline().split('-')
result = 0
len_f = len(formula)

for i in formula[0].split('+'):
    result += int(i)
for i in range(1, len(formula)):
    for j in formula[i].split('+'):
        result -= int(j)
print(result)