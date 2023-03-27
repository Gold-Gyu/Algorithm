T = int(input())


def patrol(now, e_sum):
    global min_value

    # 지금까지 구할 에너지의 합이 내가 알고 있는 최소값보다 크면 더 이상 진행할 필요가 없다.
    # 이후에 진행해봤자 합이 늘어나면 늘어났지 줄어들리가 없기 때문에 중단
    if e_sum >= min_value:
        return


    # 종료 조건
    # 모든 방을 다 방문했으면 시작지점으로 돌아간다 (종료)
    if 0 not in visited:
        min_value = min(min_value, e_sum + e[now][0])
        return

    # 현재 위치에서 갈수 있는 다음 방을 탐색
    # 내가 이전에 들른적이 없는 방을 선택
    for next_room in range(n):
        if next_room != now and visited[next_room] == 0:
            # 다음 방으로 갔다고 체크하고 길을 찾는다.
            visited[next_room] = 1
            # 다음방의 에너지양을 더해서 이동
            patrol(next_room, e_sum + e[now][next_room])
            # 다음 경우의 수를 위해서 다음방 체크 해제
            visited[next_room] = 0


for tc in range(1, T + 1):
    n = int(input())

    e = [list(map(int, input().split())) for _ in range(n)]
    # 각 방은 1번만 방문 해야되니까 방문체크
    visited = [0] * n

    # 첫번째 방은 출발시 방문했다고 처리
    visited[0] = 1
    min_value = 10000

    patrol(0, 0)

    print(f"#{tc} {min_value}")