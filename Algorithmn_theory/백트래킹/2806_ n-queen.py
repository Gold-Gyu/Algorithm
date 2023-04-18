def promising(i, j):
    # 각 방향 확인
    for di, dj in [[-1, -1], [-1, 0], [-1, 1]]: # 위에 퀸이 놓여있기 때문에 위만 확인하면된다.
        ni, nj = i + di, j + dj
        # 언제까지 가느냐면
        while 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj]:   # 다른 퀸이 있는 상황이면
                return 0        # 실패

            # 다른 퀸이 없는 상황이면
            ni, nj = ni + di, nj + dj
    return 1    # i, j에 퀸을 놓을 수 있음음

def f(i, N):
    global cnt
    if i == N: # 너가 모든행을 고려해서 N개의 퀸을 놓은 경우
        cnt += 1

    else:
        for j in range(N): # i라는 행에서 j 열을 돌면서
            if promising(i, j): # 놓을 수 있는 자리인지 확인하는 함수
                board[i][j] = 1 # 위치에 퀸 올리고
                print(board)
                f(i+1, N)       # 그 다음 행에 퀸을 놓을 수 있는지 돌린다.
                board[i][j] = 0 # 모든행을 다 고려해서 퀸을 모두 넣어봤는데 넣을 곳이 없다면 지우기
                print(board)



T = int(input())

for tc in range(1, T+1):
    N = int(input())

    board = [[0] * N for _ in range(N)]
    cnt = 0

    f(0, N)

    print(f"#{tc} {cnt}")