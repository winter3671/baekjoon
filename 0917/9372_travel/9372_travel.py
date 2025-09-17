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
        return

    if rx > ry:
        parents[rx] = ry
    else:
        parents[ry] = rx

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    parents = make_set(N + 1)

    while len(parents) > 2:
        for i in range(M):
