N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

chicken = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            chicken.append([i, j])

def dfs(start, path):
    if len(path) == M:
        result.append(path[:])
        return

    for i in range(start, len(chicken)):
        path.append(chicken[i])
        dfs(i+1, path)
        path.pop()

result = []

dfs(0, [])

delta_x = [0, 1, 0, -1]
delta_y = [1, 0, -1, 0]
delta_range = 1

find_home = False
chicken_range = 0

for lst in result:
    for chicken_house in lst:
        [x, y] = chicken_house
        for i in range(4):
            dx = x + delta_x[i]
            dy = y + delta_y[i]
            if (0 <= dx < N and 0 <= dy < N) and arr[dx][dy] == 1:
                find_home = True
