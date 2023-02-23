T = int(input())

dr = [-1,-1,-1, 0, 0, 1, 1 ,1]
dc = [-1, 0, 1, -1, -1, 0 , -1]

for tc in range(1, T+1):
    n = int(input())

    mountains = [list(map(int, input().split())) for _ in range(n)]

    # 봉우리의 개수


    # 최대높이, 최소높이
    maxV = 0
    minV = 100

    # 2차원 배열 탐색 모든 위치 r, c를 검사하는데 외각은 검사할 필요가 없다
    for r in range(n):
        for c in range(n):

            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < n:
                    if mountains[r][c] <= mountains[nr][nc]:
                        break

                else:
                    break
            # 중간에 8방향 탐색을 그만둔적이 없다면 주변이 다 나 보다 낮고 8방향이 온전히 있는 위치
            else:
                hill += 1
                maxV = mountains[r][c] if maxV < mountains[r][c] else maxV
                minV = mountains[r][c] if maxV > mountains[r][c] else minV

    if hill >= 2:
        print(f"#{tc} {maxV - minV}")

    else:
        print(f"{tc} {-1}")