A, B, V = map(int, input().split())
gap = A - B
if (V-A) % gap == 0:
    day = (V - A) // gap + 1
else:
    day = (V - A) // gap + 2

print(day)