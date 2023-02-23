
T = int(input())


# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

r = 0
c = 0



for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    stack = []


    visited[r][c] = 1

    for i in range(N*N):

        if arr[r][c] == 0:  # 0이면 우로 이동
            d = 0
            nx = r + dx[d]
            ny = c + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:    # 범위 안에 있고 방문했적이 없으면
                stack.append(arr[r][c])
                r, c = nx, ny

            else:
                break


        elif arr[r][c] == 1:  # 0이면 우로 이동
            d = 1
            nx = r + dx[d]
            ny = c + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:  # 범위 안에 있고 방문했적이 없으면
                r = nx
                c = ny
                stack.append(arr[r][c])


            else:
                break
        elif arr[r][c] == 2:  # 0이면 우로 이동
            d = 2
            nx = r + dx[d]
            ny = c + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:  # 범위 안에 있고 방문했적이 없으면
                r = nx
                c = ny
                stack.append(arr[r][c])

            else:
                break

        elif arr[r][c] == 3:  # 0이면 우로 이동
            d = 3
            nx = r + dx[d]
            ny = c + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:  # 범위 안에 있고 방문했적이 없으면
                r = nx
                c = ny
                stack.append(arr[r][c])

            else:
                break
    else:
        print(f"#{tc} {stack}")







