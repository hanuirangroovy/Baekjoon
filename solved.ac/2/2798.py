n, m = map(int, input().split())
list_n = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if list_n[i] + list_n[j] + list_n[k] <= m:
                blackjack = list_n[i] + list_n[j] + list_n[k]
                if result <= blackjack:
                    result = blackjack
print(result)

