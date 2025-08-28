N = int(input())

min_cnt = float('inf')
for i in range((N // 5)+1):
    if (N - (5*i)) % 3 == 0:
        cnt = i + ((N - (5 * i)) // 3)
        if min_cnt > cnt:
            min_cnt = cnt

if min_cnt == float('inf'):
    min_cnt = -1

print(min_cnt)