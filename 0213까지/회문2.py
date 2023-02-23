import sys
sys.stdin = open('input (15).txt', 'r')
from pprint import pprint



T = 10

for tc in range(1, T + 1):
    test = int(input())

    # 회문의 최대 길이
    ans = 1

    puzzle = [list(input()) for _ in range(100)]
    t_puzzle = list(zip(*puzzle))

    for i in range(100):
        for j in range(100 - ans):
            # 회문의 최대 길이가 100
            # 가능한 길이를 모두 검사
            # 근데 내가 지금까지 알고있는 회문의 최대 길이보다 큰거만 검사하면 되지 않을까??
            for l in range(ans, 100):
                # (i,j) 위치에서 길이 l짜리 회문을 만들기 => 가로, 세로
                # 회문의 길이가 배열의 범위를 벗어나면 안된다
                if j + l > 100:
                    break
                row = puzzle[i][j:j + l]
                col = t_puzzle[i][j:j + l]
                if row == row[::-1] or col == col[::-1]:
                    ans = l

    print(f"#{tc} {ans}")
# T = 10
#
# for tc in range(1, T+1):
# # 회문의 최대 길이
#     aa = int(input())
#     ans = 1
#
#     puzzle = [list(input()) for _ in range(100)]
#     t_puzzle = list(zip(*puzzle))  # puzzle의 전치행렬
#
#     for i in range(100):    #행
#         for j in range(100 - ans):    # 열
#             # word_row = ""
#             # word_col = ""
#             for l in range(ans, 100):
#                 # (i, j) 위치에서 길이 l 까지 회문만들기 => 가로 세로
#                 # 회문의 길이가 배열의 범위를 벗어나면 안된다
#                 if j + l > 100:
#                     break
#                 row = puzzle[i][j: j + l]
#                 col = t_puzzle[i][j: j + l]
#                 if row == row[::-1] or col == col[::-1]:
#                     ans = 1
#
#     print(f"#{tc} {ans}")

