while True:
    word = str(input())

    if word == '*':
        break

    letter_idx = [False for _ in range(26)]

    for letter in word:
        if letter == ' ':
            continue

        letter_idx[ord(letter) - ord('a')] = True

    for idx in letter_idx:
        if idx == False:
            print('N')
            break
    else:
        print('Y')