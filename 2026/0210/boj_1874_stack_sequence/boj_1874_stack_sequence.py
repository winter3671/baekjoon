'''
1. 문제 분석
주어진 수열을 만들기 위해, 1~n까지의 수를 push와 pop해서 만들어보자.

2. 풀이 방법 고안
첫번째 수를 출력하려면, 그 수까지는 무조건 +를 해야함(ex. 4)
그 다음 수가 첫번째 수보다 작으려면, 무조건 1차이로 작아져야함(ex. 3, 2)
-> 반드시 1차이일 필요는 없다. pop을 할려고 할 때 스택의 맨 위를 꺼내야한다는것만 유지하면 됨
1보다 큰 수치로 작아지면 불가능

다음수가 첫번째 수보다 크다면, 그 수까지 또 +
n이 출력이 되면, 출력된 수를 제외한 나머지 수를 역순으로 순차적으로 출력해야함
'''
n = int(input())

stack = []
cnt = 0
result = []

for _ in range(n):
    num = int(input())

    if cnt < num:
        while True:
            if cnt == num:
                stack.pop()
                result.append('-')
                break

            cnt += 1
            stack.append(cnt)
            result.append('+')

    elif cnt > num:
        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            print('NO')
            break

else:
    print(*result, sep='\n')