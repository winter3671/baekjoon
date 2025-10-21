A = int(input())
B = int(input())
C = int(input())
result = A*B*C
result = str(result)
result_idx = [0] * 10
for i in result:
    result_idx[int(i)] += 1

for i in result_idx:
    print(i)