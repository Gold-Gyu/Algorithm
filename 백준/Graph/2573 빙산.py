from collections import deque
from pprint import pprint

"""
반례

5 7
0 0 0 0 0 0 0
0 3 3 2 3 3 0
0 4 0 4 0 3 0
0 0 0 0 4 3 0
0 0 0 0 0 0 0
0


5 7
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 10 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0


5 7
0 0 0 0 0 0 0
0 3 3 1 3 3 0
0 4 0 4 0 3 0
0 0 0 0 4 3 0
0 0 0 0 0 0 0
1


5 7
0 0 0 0 0 0 0
0 3 6 3 6 7 0
0 3 0 0 0 10 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
2


5 7
0 0 0 0 0 0 0
0 3 6 0 6 7 0
0 3 0 0 0 10 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0


5 7
0 0 0 0 0 0 0
0 9 8 9 8 9 0
0 9 8 9 8 9 0
0 9 8 9 8 9 0
0 0 0 0 0 0 0
0


5 7
0 0 0 0 0 0 0
0 9 8 3 8 9 0
0 9 8 0 8 9 0
0 9 8 9 8 9 0
0 0 0 0 0 0 0
5


5 5
0 0 0 0 0
0 1 0 1 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0

7 7
0 0 0 0 0 0 0
0 1 1 0 1 1 0
0 1 9 1 9 1 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 0 1 1 1 0 0
0 0 0 0 0 0 0
2

5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0

"""
def bfs_final_check(i, j):  # 빙산 덩어리 갯수를 세주는 함수

    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        size = len(q)
        for x in range(size):
            r, c = q.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if is_valid(nr, nc) and arr[nr][nc] and visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    q.append((nr, nc))

def is_valid(r, c): # 4방향 탐색 중 범위를 벗어나지 않는 조건
    return 0 <= r < N and 0 <= c < M

def bfs_check_zero(i, j):   # 해당 위치에 0의 개수가 몇개 있는지 나타내는 함수

    q = deque() # 데큐 생성
    r, c = i, j # 시작 위치
    q.append((r, c))    # 큐에 넣기

    while q:
        size = len(q)   # 큐에 넣은 만큼 반복 => 내가 갈 수 있는 곳들 개수 만큼
        for v in range(size):   #
            r, c = q.popleft()  # 갈 곳 꺼낸다
            for k in range(4):  # 갈 곳의 위치에서 4방향 탐색
                nr = r + dr[k]
                nc = c + dc[k]
                if is_valid(nr, nc) and arr[nr][nc] == 0:   # 범위안에 있고 4방향 중 0이 있으면
                    visited[r][c] += 1  # 1씩 더해준다.

# 4방향 탐색을 위한 델타배열 생성
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]


ans = 0 # 답 도
year = 0    # 년수 계산
flag = False    # 중간에 빠져 나오기 위한 체크포인트 역할

while True:
    visited = [[0] * M for _ in range(N)]  # 방문체크 함수 계속 초기화
    # 1. 주변에 0이있는 갯수를 나타내는 visited 함수 만들기
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                bfs_check_zero(i, j)

    # arr에서 visited뺴주기
    # 단 -값이 나오면 0으로 바꿔주기
    for i in range(N):
        for j in range(M):
            # 첫 번째 할 일
            if visited[i][j]:
                arr[i][j] = arr[i][j] - visited[i][j]
                if arr[i][j] < 0:
                    arr[i][j] = 0
    # 이 전체과정이 끝났을 때
    year += 1   # 1년이 지난거임
    # visited 초기화
    # 방문함수 초기화 이유 :
    # 밑에서 방문함수를 사용하여 빙산 덩어리가 몇개인지 확인을 하기 때문에
    # 방문함수를 다시 초기화해서 사용해야한다.
    visited = [[0] * M for _ in range(N)]

    # 1년이 지난 빙산(arr) 전체가 몇 조각인지 확인하기
    # 2개 미만이다가 0개가 되면 답은 0
    # 2개가 되면 그동안의 year 출력
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] and visited[i][j] == 0:    # arr에 0이아닌 숫자가 있고 방문한적이 없는 곳이면
                bfs_final_check(i, j)   # 함수안에들어가서 4방향으로 연결된 곳들은 모두 방문처리
                cnt += 1    # 빙산 덩어리 개수 +1
                if cnt >= 2:    # 만약 빙산 덩어리가 2개가 되면
                    ans = year  # 몇 년동안의 시간이 걸렸는지 출력
                    flag = True
                    break   #  for j

        if flag:
            break # for i
    if flag:
        break # while

    if cnt == 0: # 만약 빙산덩어리가 2개가 되보지도 못하고 모두 사라지면
        # ans = 0 # 0 출력, 굳이 없어도 초기 ans값을 0으로했기 떄문에 상관없긴함
        break

print(ans)
