words_list = []
for _ in range(3):
    words_list.append(input())

for i in range(3):
    if words_list[i] not in ['Fizz', 'Buzz', 'FizzBuzz']:
        target = int(words_list[i]) + 3 - i

result = target

if target % 3 == 0:
    if target % 5 == 0:
        result = 'FizzBuzz'
    else:
        result = 'Fizz'
elif target % 5 == 0:
    result = 'Buzz'

print(result)