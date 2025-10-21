N = int(input())
F = int(input())

gap = N % 100
N -= gap

result = 0

for i in range(100):
   if (N + i) % F == 0:
       result = i
       break

if result // 10 == 0:
    result = '0' + str(result)

print(result)