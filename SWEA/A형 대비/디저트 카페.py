import sys
sys.stdin = open("디저트 카페.txt", "r")


# 이동 순서
# 우하, 좌하, 좌상, 우상
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

# 방향 설정
RD = 0 # 우하
LD = 1 # 좌하
LU = 2 # 좌상
RU = 3 # 우상

# 해당 지역을 벗어나서는 안된다.
def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n



# 방문체크 (visited)
# 현재 나의 방향(dir)
# 좌표정보(now)
# now[0] = r, now[1] = c
# 중복처리 하는 법 우하 방향으로 항상 시작

def travel(visited, dir, now):

    global answer
    # 종료조건
    # 다시 출발점으로 돌아온 경우
    if now == start and dir == RU:
        # 도착했을때 방향이 우상을 바라봐야 자기 자리로 돌아온 것이다.
        answer = max(answer, len(visited))

    # 재귀 호출

    # 내가 고려해야하는 상황 2가지
    # 현재 방향으로 쭉 가거나(dir + 0)
    # 다음방향으로 바꿔서 가거나
    # 방향 바뀌는 순서가 우하, 좌하, 좌상, 우상 순서 고정
    for d in range(2):
        dir += d

        # 방향이 더이상 바꾸면 안될 때
        if dir == 4:
            break

        nr = now[0] + dr[dir]
        nc = now[1] + dc[dir]

        #다음위치로갈껀데, 다음위치가 범위 안이고
        # 전에 먹었던 디저트 종류도 아니어야한다.
        if is_valid(nr, nc) and cafe_map[nr][nc] not in visited:
            # 디저트 먹고 다음 탐색
            visited.append(cafe_map[nr][nc])
            travel(visited, dir, (nr, nc))
            visited.pop()

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    cafe_map = [list(map(int, input().split())) for _ in range(n)]

    # 일단 갈 수 없다고 진행
    # 더 이상 카페로 갈 길이 없다고 생각하여 -1로 시작
    answer = -1

    # 모든 위치에서 탐색시작
    # 근데 탐색 방향은 오른쪽 아래로만 한다(길 중복을 방지하기 위해서)
    # 밑에서 출발하는 경우(위쪽 방향으로 오는 경우 충복 체크안해도되기 때문)
    for r in range(n):
        for c in range(n-1):    # n-1인 이유
            start = (r, c)
            # 방문체크, 방향, 내 위치
            travel([], RD, (r, c))
    print(f"#{tc} {answer}")