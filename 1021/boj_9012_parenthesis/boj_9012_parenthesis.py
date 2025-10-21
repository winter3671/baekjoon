T = int(input())
for tc in range(1, T+1):
    line = input()
    stack = []
    result = True
    for i in line:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                result = False

    if stack:
        result = False

    if result:
        print('YES')
    else:
        print('NO')