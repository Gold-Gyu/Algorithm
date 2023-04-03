T = int(input())

for tc in range(1, T+1):
    n = int(input())
    hex = int(input(), 16)  # 16진수
    maxV = 0
    cnt = 0

    # 16진수 2진수로 바꾸기
    # 16진수의 길이가 n일 때 2진수로 바꾸면 n * 4
    for i in range(4 * n):
        if hex & (1 << i): # i번째 비트와 비교했을 떄 결과가 0이 아니면
            cnt += 1
            if maxV < cnt:
                maxV = cnt

        else:
            cnt = 0
    print(f"#{tc} {maxV}")