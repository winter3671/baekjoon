while True:
    n = int(input())
    if n == 0:
        break

    # 1~n까지의 합을 출력 -> n(n+1) // 2

    print(n * (n + 1) // 2)