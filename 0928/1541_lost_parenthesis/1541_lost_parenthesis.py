expression = input()

new_exp = []
num = ''
is_minus = False    # 앞에 '-' 기호가 있었는지 확인
for i in expression:
    if i not in ['+', '-']:     # i가 숫자라면
        if num is False:
            if i == '0':    # 처음 오는 수가 0이라면
                continue    # 0은 생략
            else:           # 처음 온 수가 0이 아니라면
                num += i    # num에 저장
        else:
            num += i

    else:   # i가 연산기호라면
        new_exp.append(num)     # 기존에 저장한 num을 new_exp에 저장하고
        num = ''        # num은 초기화
        if i == '-':
            new_exp.append(i)
            is_minus = True
        else:       # 기호가 '+'이고,
            if is_minus:    # 앞에 '-'기호가 왔다면
                new_exp.append('-')     # '-'기호로 변환
            else:       # '-'기호가 온 적이 없다면
                new_exp.append('+')     # 그대로 '+'를 저장

new_exp.append(num)

result = 0
for i in range(len(new_exp)):
    if i == 0:
        result += int(new_exp[i])

    if new_exp[i] == '+':
        result += int(new_exp[i+1])

    elif new_exp[i] == '-':
        result -= int(new_exp[i+1])

print(result)