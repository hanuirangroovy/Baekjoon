n = int(input())
string = input()
result = 0
for i in range(n):
    result += (ord(string[i])-96)*(31 ** i)
print(result % 1234567891)