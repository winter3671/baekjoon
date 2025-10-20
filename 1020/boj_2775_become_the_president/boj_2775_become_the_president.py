'''
1. 문제 분석
1층1호: 1
1층2호: 1+2
1층3호: 1+2+3
1층4호: 1+2+3+4
2층1호: 1
2층2호: 1 + 1+2
2층3호: 1 + 1+2 + 1+2+3
3층1호: 1
3층2호: 1 + 1+1+2
3층3호: 1 + 1+1+2 + 1+1+2+1+2+3
'''
T = int(input())
for tc in range(1, T+1):
    k = int(input())
    n = int(input())

    arr = [0 for _ in range(14)]
    for i in range(14):
        arr[i] = i+1

    floar = 0
    while floar < k:
        for i in range(13, -1, -1):
            arr[i] = sum(arr[j] for j in range(i+1))
        floar += 1

    print(arr[n-1])