N = int(input())
stack = []
for _ in range(N):
    line = input()

    if line[:4] == 'push':
        stack.append(line[5:])

    elif line == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif line == 'size':
        print(len(stack))

    elif line == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif line == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
