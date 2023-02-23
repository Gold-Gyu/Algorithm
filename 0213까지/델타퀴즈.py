import random

from pprint import pprint

# 퀴즈
# 행5 * 열6 값을 임의로 할당(random)
# 2차원 배열의 모든 원소를 순회하면서 짝수인 원소의 개수를 세는 프로그램

# 행
N = 5

# 열

M = 6

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 리스트 만들기
arr = [[random.randrange(1, 11) for _ in range(M)] for _ in range(N)]

# 행 우선 순회
cnt = 0
for x in range(N):
    for y in range(M):
        if arr[x][y] % 2 == 0:
            cnt += 1

        # for d in range(4):
        #     nx = x + dx[d]
        #     ny = y + dy[d]
        #
        #     if 0 <= nx < N and 0 <= ny < N:


print(cnt)



