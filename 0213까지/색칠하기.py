T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 색칠 횟수

    paper = [[0] * 10 for _ in range(10)]

    # 겹친 칸 갯수(보라색)

    purple_count = 0

    for tc2 in range(N):
        # 색칠정보 입력
        from_i, from_j, to_i, to_j, color = map(int, input().split())

        for i in range(from_i, to_i + 1): # 색칠 시작 행~ 색칠 끝 행
            for j in range(from_j, to_j +1): # 색칠 시작 열 ~ 색칠 끝 열
                if paper[i][j] == 0: #색칠이 없다

                # 내가 지금 i j에 색칠하려고하는데
                # 1 내가 칠혀라녀는 칸에 색기 없다 => 색칠
                    paper[i][j] = color

                # 2 내가 칠하려는 칸에 색이 있다 => 색이 겹치니까 보라색 칸이다.
                else:
                    purple_count += 1
    print(f"#{tc}")



