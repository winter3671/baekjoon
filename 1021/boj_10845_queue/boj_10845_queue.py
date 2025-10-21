N = int(input())
q = []
for _ in range(N):
    line = input()

    if line[:4] == 'push':
        q.append(line[5:])

    elif line == 'pop':
        if q:
            print(q.pop(0))
        else:
            print(-1)

    elif line == 'size':
        print(len(q))

    elif line == 'empty':
        if q:
            print(0)
        else:
            print(1)

    elif line == 'front':
        if q:
            print(q[0])
        else:
            print(-1)

    elif line == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)