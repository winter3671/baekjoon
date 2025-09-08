def combinations(n, lev, step):
    if lev == M:
        print(' '.join(map(str, q)))
        return

    for i in range(step, n+1):
        q.append(i)
        combinations(n, lev + 1, i+1)
        q.pop()

N, M = map(int, input().split())
q = []
combinations(N, 0, 1)