import random

from pprint import pprint

# 행
n = 5

# 델타 배열
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0 -1, 1]

# 함수 만들기

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n

arr = [[random.randrange(1, 11) for _ in range(n)] for _ in range(n)]

pprint(arr)

# 절대값의 총합
abs_sum = 0

# 행 우선

for x in range(n):
    for y in range(n):
        # 현재위치(x, y)
        now = arr[x][y]
        print(f"arr[{x}][{y}] : {arr[x][y]}")

        # 4 방향 탐색을 하면서 이웃한 원소의 차이의 절대값의 합을 구한다
        # 주의할 점 : 상하좌우로 움직일 때 유효한 범위(인덱스) 인지 꼭 확인

        temp_abs = 0 # 현재 위치에서 절대값의 합

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if is_valid(nx, ny): # 함수를 만들었을 떄 사용


            # 함수를 안만들면 아래 처럼해야함
            # if 0 <= nx < n and 0 <= ny < n:
                # 절대값 계산
                temp_abs += abs(arr[x][y] - arr[nx][ny])
            abs_sum += temp_abs

print(f"ans : {abs_sum}")

# 퀴즈
# 행5 * 열6 값을 임의로 할당(random)
# 2차원 배열의 모든 원소를 순회하면서 짝수인 원소의 개수를 세는 프로그램