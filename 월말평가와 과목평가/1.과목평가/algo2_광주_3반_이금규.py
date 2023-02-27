T = int(input())

arr = [[0] * 10 for _ in range(10)] # 10 * 10 배열 완성


for tc in range(1, T+1):
    N = int(input())
    r, c = map(int, input().split()) # 망치위치


    for tc2 in range(N):
        A, B, K = map(int, input().split()) # 두더지의 좌표와 K

        answer = 0 # 잡은 개수
        for i in range(K+1): # k초 안에 잡아야하기 때문에

            if c > B: # 두더지의 y값이 더 크면 좌로 이동
                r = r + 0
                c = c - 1
                if r == A and c == B: # 이때 망치와 두더지의 위치가 같으면 잡음 + 1
                    answer += 1

            elif c < B: # 두더지의 y값이 더 크면 우로 이동
                r = r + 0
                c = c + 1
                if r == A and c == B: # 이때 망치와 두더지의 위치가 같으면 잡음 + 1
                    answer += 1

            else:   # y값이 같으면 상하 확인

                if r > A: # 두더지의 x값이 더 적으면 상
                    r = r - 1
                    c = c + 0
                    if r == A and c == B: # 이때 망치와 두더지의 위치가 같으면 잡음 + 1
                        answer += 1

                elif r < A: # 두더지의 x 값이 더 크면 하
                    r = r + 1
                    c = c + 0
                    if r == A and c == B: # 이때 망치와 두더지의 위치가 같으면 잡음 + 1
                        answer += 1

                else:       # 두더지와 망치의 x, y 값이 같으면
                    if r == A and c == B: # 이때 망치와 두더지의 위치가 같으면 잡음 + 1
                        answer += 1

    print(f"#{tc} {answer}")