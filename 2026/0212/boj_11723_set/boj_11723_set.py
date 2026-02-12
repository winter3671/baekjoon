import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    command = input().split()
    if len(command) == 1:
        if command[0] == 'all':
            S = set(range(1, 21))
        else:  # empty
            S = set()
    else:
        order, num = command[0], int(command[1])

        if order == 'add':
            S.add(num)
        elif order == 'remove':
            S.discard(num)
        elif order == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif order == 'toggle':
            if num in S:
                S.discard(num)
            else:
                S.add(num)

