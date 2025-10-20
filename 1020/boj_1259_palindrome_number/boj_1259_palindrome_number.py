while True:
    num = input()
    if num == '0':
        break

    rev_num = reversed(num)
    if num == ''.join(list(rev_num)):
        print('yes')
    else:
        print('no')