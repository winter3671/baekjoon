N = int(input())
count = [0 for _ in range(10001)]

for i in range(N):
    count[int(input())] += 1

for num in range(1, 10001):
    if count[num] > 0:
        for _ in range(count[num]):
            print(num, end="\n")