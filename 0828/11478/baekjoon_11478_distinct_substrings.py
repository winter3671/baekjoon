# word = input()
# arr = []
#
#
# for i in range(len(word)):
#     for j in range(len(word)-i):
#         if word[i:i+1+j] not in arr:
#             arr.append(word[i:i+1+j])
#
# print(len(arr))

word = input()
check = set()

for i in range(len(word)):
    for j in range(len(word)-i):
        check.add(word[i:i+1+j])

print(len(check))