import sys
sys.stdin = open("input.txt")

word = input()
count = len(word)

sample = {'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z='}
for i in range(len(word)-1):
    if word[i:i+2] in sample:
        count -= 1

for i in range(len(word)-2):
    if word[i:i+3] == 'dz=':
        count -= 1

print(count)
