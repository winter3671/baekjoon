N = int(input())
points_lst = [tuple(map(int, input().split())) for _ in range(N)]
points_lst.sort()

for point in points_lst:
    print(" ".join(map(str, point)))