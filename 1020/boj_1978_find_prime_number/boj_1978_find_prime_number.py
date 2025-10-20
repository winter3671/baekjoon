N = int(input())
num_lst = list(map(int, input().split()))
cnt = 0

for num in num_lst:
    if num == 1:
        continue

    for i in range(2, num // 2 + 1):
        if num % i == 0:
            break
    else:
        cnt += 1

print(cnt)