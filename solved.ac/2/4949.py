while True:
    word = input()
    result = []
    for i in word:
        if i == '[' or i == '(':
            result.append(i)
        elif i == ']':
            if len(result) != 0 and result[-1] == '[':
                result.pop()
            else:
                result.append(']')
                break
        elif i == ')':
            if len(result) != 0 and result[-1] == '(':
                result.pop()
            else:
                result.append(')')
                break
    if word == ".":
        break
    if len(result) == 0 :
        print('yes')
    else :
        print('no')