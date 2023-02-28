# 문제를 빠르게 읽고
# 테스트케이스
# 정답처리 부분과 조건 추가 부분이 중요하다.


# q, visited 생성 및 초기화
# q의 초기데이터(들)삽입 + visited 표시 + 필요처리

# while q:
    # q에서 한개 꺼내기 (※ 정답처리는 이 곳에서)
    # visited[ans] < visited[c] or visited[ans] == visited

    # 4/8방향, 미방문 + ※  조건이 맞으면
        # q 삽입, visited 표시

def f(adjL, sp):
    visited = [0] * 101
    q = []
    q.append(sp)
    visited[sp] = 1
    maxV = 0
    while q:
        t = q.pop(0)
        for i in adjL[t]:
            if not visited[i]:
                visited[i] = visited[t] + 1
                q.append(i)
                if maxV < visited[i]:
                    maxV = visited[i]

    for i in range(101):
        if visited[i] == maxV:
            box.append(i)

    return max(box)


T = 1
for tc in range(1, T + 1):
    length, sp = map(int, input().split())
    lst = list(map(int, input().split()))
    box = []
    adjL = [[] for _ in range(101)]
    for i in range(length // 2):
        start, to = lst[i * 2], lst[i * 2 + 1]
        adjL[start].append(to)

    ans = f(adjL, sp)
    print(f"#{tc} {ans}")
