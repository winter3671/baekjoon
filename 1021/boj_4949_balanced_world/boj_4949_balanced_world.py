import sys

while True:
    line = sys.stdin.readline().rstrip()

    if line == '.':
        break

    stack = []
    balance = True
    for spell in line:
        if spell == '.':
            break

        if spell in '([':
            stack.append(spell)
        elif spell == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    balance = False
            else:
                balance = False
        elif spell == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    balance = False
            else:
                balance = False

    if stack:
        balance = False

    if balance:
        print('yes')
    else:
        print('no')