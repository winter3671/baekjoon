import sys
sys.stdin = open('input.txt')

def make_set(x):
    parents = [i for i in range(x)]
    return parents

def find_set(x):
    if x == parents[x]:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry:
        return False

    if rx > ry:
        parents[rx] = ry
        return True
    else:
        parents[ry] = rx
        return True

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    parents = make_set(N + 1)

    count = 0
    for a, b in arr:
        if len(set(parents)) - 1 == 1:      # parents에 0을 제외하고 숫자가 1종류면
            break                           # break

        if union(a, b):                     # a, b가 union에 성공하면
            count += 1

    print(count)