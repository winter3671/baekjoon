N = int(input())
arr = [[" " for _ in range(2**N)] for _ in range(2**N)]

def star(n, x, y):
    if n == 0:
        arr[x][y] = '*'
        return

    star_start = 2 ** (n-1)

    star(n-1, x, y)
    star(n-1, x, y + star_start)
    star(n-1, x + star_start, y)

star(N, 0, 0)

for stars in arr:
    print("".join(stars).strip())