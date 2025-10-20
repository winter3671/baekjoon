L = int(input())
words = input()
uni_words = [ord(i) - ord('a') + 1 for i in words]

hash_sum = 0
for i in range(L):
    hash_sum += uni_words[i] * 31**i

hash_sum %= 1234567891

print(hash_sum)