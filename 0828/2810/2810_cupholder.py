N = int(input())
words = input()

count = N+1
check = 0

while check < N:
    if words[check:check+2] == 'LL':
        count -= 1
        check += 1
    check += 1
    
if count > N:
    count = N

print(count)