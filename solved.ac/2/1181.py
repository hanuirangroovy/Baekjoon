n = int(input())
word = []
list_word = [[] for _ in range(51)]
for i in range(n):
    word.append(input())
word_s = list(set(word))
for i in range(len(word_s)):
    list_word[len(word_s[i])].append(word_s[i])
for i in range(51):
    list_word[i].sort()
result = []
for i in range(len(list_word)):
    if len(list_word) >= 1:
        for j in range(len(list_word[i])):
            result.append(list_word[i][j])
for i in result:
    print(i)
