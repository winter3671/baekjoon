N = int(input())
people_lst = [tuple(input().split()) for _ in range(N)]
people_lst.sort(key=lambda x:int(x[0]))

for person in people_lst:
    print(" ".join(person))