cnt = 0
while True:
    try:
        word = input()

        if word == 'gum gum for jay jay':
            cnt += 1

    except EOFError:
        break

print(cnt)