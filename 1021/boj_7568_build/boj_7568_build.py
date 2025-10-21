N = int(input())
data_lst = []
for _ in range(N):
    data_lst.append(tuple(map(int, input().split())))

result = []

for data in data_lst:
    x, y = data
    cnt = 1
    for another_data in data_lst:
        x0, y0 = another_data
        if data != another_data:
            if x0 > x and y0 > y:
                cnt += 1
    result.append(cnt)

print(" ".join(map(str, result)))