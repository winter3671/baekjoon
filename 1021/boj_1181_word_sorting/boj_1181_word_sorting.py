N = int(input())
words_set = set()
for _ in range(N):
    words_set.add(input())

words_list = list(words_set)
words_list.sort()
words_list.sort(key=lambda x:len(x))

for word in words_list:
    print(word)