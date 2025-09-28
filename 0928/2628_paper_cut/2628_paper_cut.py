X, Y = map(int, input().split())
N = int(input())
cut_list = [tuple(map(int, input().split())) for _ in range(N)]

cut_x = [0, X]
cut_y = [0, Y]

for a, b in cut_list:
    if a == 1:
        cut_x.append(b)
    elif a == 0:
        cut_y.append(b)

cut_x.sort()
cut_y.sort()

max_x = 0
max_y = 0

for i in range(1, len(cut_x)):
    max_x = max(max_x, cut_x[i] - cut_x[i-1])
for i in range(1, len(cut_y)):
    max_y = max(max_y, cut_y[i] - cut_y[i-1])

print(max_x * max_y)