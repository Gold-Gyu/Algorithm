import sys
sys.stdin = open('sample_input (1).txt', 'r')

# 쌓여있는 막대기 수 cnt

T = int(input())

for tc in range(1, T+1):
    st = input()
    ans = 0
    cnt = 0
    for i in range(len(st)):
        if st[i] == "(":            # 막대기 시작 or 레이저
            cnt += 1
        else:                       # ")" => 바로 앞의 기호를 확인해야하는 경우이다.
            if st[i-1] == "(":      # 레이저이면
                cnt -= 1
                ans += cnt
            else:                   # 막대기의 끝
                cnt -= 1
                ans += 1


    print(f"#{tc} {ans}")