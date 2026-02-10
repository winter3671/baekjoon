'''
1. 문제 분석
첫번째 줄에 플레이어의 수 p와 정원 m이 주어짐
두번째줄부터, 플레이어의 레벨과 닉네임이 공백을 두고 주어짐

플레이어는 위에서부터 방을 보면서, 방장의 레벨 +-10까지의 방에 들어갈 수 있음
입장가능한 방이 없을 경우, 새로운 방을 생성
방 정원이 모두 차면 게임을 시작시킴

2. 풀이 방법 고안
각 방을 만들고, 그 방에 들어간 플레이어의 정보를 저장해두고 있어야 함
튜플형태로 레벨과 닉네임을 저장
튜플의 0번째 인덱스의 레벨(tup[0][0])을 기준으로 입장 가능한지 판단 가능
입장 시 정원이 다 차면 다음 방으로 들어가야함.
모든 플레이어 입장 후, 각 방을 닉네임에 대해 정렬시키고, 출력
'''
p, m = map(int, input().split())
gamerooms = []

for _ in range(p):
    l, n = map(str, input().split())
    l = int(l)

    if not gamerooms:   # 게임룸이 비었을 때
        gamerooms.append([(l, n)])
    else:   # 게임 룸에 하나 이상의 방이 있을 때
        for room in gamerooms:  # 각 방을 돌면서,
            if len(room) < m and room[0][0] - 10 <= l <= room[0][0] + 10:   # 방의 정원이 다 차지 않았고 방장의 레벨 += 10이라면
                room.append((l, n))     # 방에 참가
                break
        else:   # 게임룸 전체를 돌았는데도 방에 참가하지못하면
            gamerooms.append([(l, n)])    # 방을 생성하고, 본인이 참가

for room in gamerooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')

    room.sort(key=lambda x: x[1])
    for player in room:
        print(*player, sep=' ')