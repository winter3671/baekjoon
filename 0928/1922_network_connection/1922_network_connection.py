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

    if rx < ry:
        parents[ry] = rx
    else:
        parents[rx] = ry


N = int(input())
M = int(input())
cost_list = [tuple(map(int, input().split())) for _ in range(M)]
cost_list.sort(key=lambda x: x[2])

parents = make_set(N + 1)

cnt = 0
cost = 0

for x, y, w in cost_list:
    if find_set(x) != find_set(y):
        union(x, y)
        cnt += 1
        cost += w

    if cnt == N - 1:
        continue

print(cost)