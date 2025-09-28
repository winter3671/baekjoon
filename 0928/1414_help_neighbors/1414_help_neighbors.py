# import sys
# sys.stdin = open('input.txt')

def make_set(x):
    return [i for i in range(x)]

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
        parents[ry] = rx
    elif rx < ry:
        parents[rx] = ry


# T = int(input())
# for tc in range(1, T+1):
N = int(input())
arr = [input() for _ in range(N)]
edges = []
sum_arr = 0

for i in range(N):
    for j in range(N):
        if ord('a') <= ord(arr[i][j]) <= ord('z'):
            sum_arr += ord(arr[i][j]) - ord('a') + 1
            if arr[i][j] != '0' and i != j:
                edges.append([i, j, ord(arr[i][j]) - ord('a') + 1])
        elif ord('A') <= ord(arr[i][j]) <= ord('Z'):
            sum_arr += ord(arr[i][j]) - ord('A') + 27
            if arr[i][j] != '0' and i != j:
                edges.append([i, j, ord(arr[i][j]) - ord('A') + 27])

edges.sort(key=lambda x: x[2])

parents = make_set(N)
cnt = 0
result = 0

for x, y, w in edges:
    if find_set(x) != find_set(y):
        union(x, y)
        cnt += 1
        result += w

    if cnt == N - 1:
        continue

if cnt == N - 1:
    print(sum_arr - result)
elif cnt < N - 1:
    print(-1)

