import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    words = input()
    alpha_cnt = [0] * 26      # 알파벳 26개에 해당하는 공간 생성
    result = ""

    for word in words:
        alpha_cnt[ord(word) - 65] += 1      # A를 alpha_cnt의 첫번째에 넣고, 순서대로 갯수를 셈

    if len(words) % 2 == 0:     # 단어가 짝수일 경우
        for i in alpha_cnt:
            if i % 2 == 1:      # 모든 알파벳이 짝수 개가 아니라면 실패
                result = "I'm Sorry Hansoo"
                break
        else:
            for idx in range(26):   # 단어 절반을 나열하고
                result += chr(idx + 65) * (alpha_cnt[idx] // 2)
            result += result[::-1]      # 그것을 뒤집은 단어와 합함

    else:       # 단어가 홀수일 경우
        cnt = 0
        for i in alpha_cnt:
            if i % 2 == 1:
                cnt += 1
            if cnt == 2:        # 알파벳의 갯수 중 홀수가 2개 이상이면 실패
                result = "I'm Sorry Hansoo"
                break
        else:
            for idx in range(26):
                if alpha_cnt[idx] % 2 == 1:
                    odd_idx = idx
                result += chr(idx + 65) * (alpha_cnt[idx] // 2)
            result = result + chr(odd_idx + 65) + result[::-1]  # 단어 절반 + 홀수갯수였던 알파벳 + 단어 절반의 reverse

    print(result)