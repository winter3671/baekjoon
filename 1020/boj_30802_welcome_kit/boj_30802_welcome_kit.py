N = int(input())
size_lst = list(map(int, input().split()))
T, P = map(int, input().split())

cnt = 0
for num in size_lst:
    if num % T != 0:
        cnt += (num // T) + 1
    else:
        cnt += num // T
print(cnt)

print(N // P, N % P)