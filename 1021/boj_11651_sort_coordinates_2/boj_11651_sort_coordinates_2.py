N = int(input())
points_lst = [tuple(map(int, input().split())) for _ in range(N)]
points_lst.sort()
points_lst.sort(key=lambda x:x[1])

for point in points_lst:
    print(" ".join(map(str, point)))