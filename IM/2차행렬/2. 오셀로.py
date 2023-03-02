# 파리퇴치
# sum
# 인덱스 일부에 접근하고
# 최대최소랑 비교하기
# 델타를 써서 확장해가는 풍선팡, 오목
# black = 1
# white = 2
# OP = [0, 2, 1]
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     board = [[0] * (N+2) for _ in range(N+2)]
#     board[N//2][N//2] = white       # 중앙지점
#     board[N // 2][N // 2 + 1] = black
#     board[N // 2 + 1][N // 2] = black
#     board[N // 2 + 1][N // 2 + 1] = white
#     for _ in range(M):
#         j, i, bw = map(int, input().split())
#         # 각 방향으로 뒤집을 수 있는 경우 찾기
#         board[i][j] = bw
#         for di, dj in [[]]
#             ni, nj = i + di, j + dj
#             tmp = []        # 다른 색 돌의 좌표 저장
#             while board[ni][nj] == OP[bw]:
#                 tmp.append((ni, nj))
#                 ni, nj = ni + di, nj + dj
#             if board[ni][nj] == bw:    # 놓은 돌과 같은 색을 만나서 중단된 경우
#                 for p, q in tmp:
#                     board[p][q] = bw
#
#     bcnt = wcnt = 0
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if board[i][j] == black:
#                 bcnt += 1
#             elif board[i][j] == white:
#                 wcnt += 1
#     print(f"#{tc} {bcnt} {wcnt}")

