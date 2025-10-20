a, b = map(int, input().split())
gcd_num = min(a, b)
gcd = 0
for i in range(1, gcd_num + 1):
    if a % i == 0 and b % i == 0:
        gcd = max(gcd, i)

lcm_max = max(a, b)
lcm_min = min(a, b)
for i in range(1, lcm_min + 1):
    if lcm_max * i % lcm_min == 0:
        lcm = lcm_max * i
        break

print(gcd)
print(lcm)