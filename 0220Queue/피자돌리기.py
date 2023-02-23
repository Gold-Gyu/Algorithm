import sys
sys.stdin = open('sample_input(1) (2).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))

    # 다음에 꺼내올 피자의 번호
    next_i = 0

    # 오븐
    oven = [0] * 1000
    ovfront = ovrear = -1

    # 오븐에 차례대로 피자를넣기
    for i in range(N):
        ovrear += 1
        oven[ovrear] = [i, C[i]]
        next_i += 1
    print(oven)
        # 오븐에 피자를 넣을 때 피자 번호를 같이 넣기

    # 오븐에 남아있는 피자 개수 확인방법
    remain = n
    # 마지막에 꺼낸 피자의 번호
    last_index = -1
    ovfront -= 1
    # 피자의 치즈가 모두 녹을 때까지 반복
    while True:
        # 피자를 꺼내서
        ovfront += 1
        i, C = oven[ovfront]
        C //= 2
        if C != 0:
            ovrear += 1
            oven[ovrear] = [i, C]

        else:
            if next_i < m:
                ovrear += 1
                oven[ovrear] = [next_i, ]
        if oven[ovfront] == 0:
            ovrear += 1
            oven[ovrear] = C[next_i]
            next_i += 1

            if
        # 치즈를 녹이고

        # 치즈가 0이 되면

            # 현재 오븐의 자리에 남은 피자 하나 꺼내서 넣기
                # 꺼내보니 넣을 피자가 없을 떄
                # 오븐에 남은 피자도 없는 상황이 온다.
                # 현재 피자의 번호가 답이 된다
                # 반복종료


        # 치즈가 0 이 아니면 다시 넣기