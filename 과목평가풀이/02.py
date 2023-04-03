T = int(input())
"""
i : 현재방의 번호
s : 지금까지 사용한 배터리의 양
selected : 지금까지 들렸던 방 번호
"""

def solve(i, s, selected):

    global minV
    # 가지치기
    if minV < s:
        return

    # 추가된 문제 조건 : b를 a보다 먼저 방문하면 안된다.
    # a를 간적이 없는데 b를 갔다? => 안된다.
    if a not in selected and b in selected:
        return


    # 종료조건
    # 방을 n번 선택해야한다.
    if len(selected) == n:
        # 처음 방으로 돌아가야한다.
        minV = min(minV, s + arr[i][0])
        return

    # 재귀호출
    # 내가 지금까지 들르지 않았떤 방을 골라서 가면된다.
    for next in range(n):
        if next not in selected:
            solve(next, s + arr[i][next], selected + [next])

for tc in range(1, T+1):
    n = int(input())

    # arr[i][j] = i번 방에서 j 번 방으로 가는데 사용하는 배터리 양
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 반드시 a를 거치고 나서 b를 가야한다.
    a, b = map(int, input().split())
    minV = n * 100
    # 위치는 0에서 시작, 시작지점 방문처리해서 마지막에 들르도록
    solve(0, 0, [])
    print(f"#{tc} {minV}")
