import sys
sys.stdin = open('sample_input(2).txt', 'r')
from pprint import pprint

def gogo(r, c, n): # n은 원소의 개수,

    # 방문배열 만들기
    visited = [[0] * n for _ in range(n)]
    # 빈스택 생성
    stack = []
    # 현재지점 방문했다고 도장찍기 그러나 내가 시작했던 지점이 1로바껴서 다시 돌아갈 수 없을 수 있기 떄문에 안한다.
    # visited[r][c] = 1

    while True:

        for i in range(n):
            for j in range(n):
                if (i, j)  == (r, c):
                    print("★", end = " ")
                else:
                    print(visited[i][j], end = " ")
            print()
        print()


        if arr[r][c] == 3:
            return 1


        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] != 1 and not visited[nr][nc]: # 1인 아닌 이유는 벽이 아니어야하기 떄문, visited는 방문한적이 없어야하기 때문
                stack.append((r, c)) # 다음위치로 가기 전에 현재 위치를 저장 # **튜플로 들어감**
                visited[nr][nc] = 1 # 다음위치 방문도장 쾅
                r, c = nr, nc # 다음위치로 이동
                break
        else: # 스택이 비어있지 않다면 하나 꺼내서 되돌아가기
            if stack:
                r, c = stack.pop() # 튜플을 꺼냄
            else: # 스택이 비어있다면 내가 갈 수 있는 길은 모두 간거다.
                break
    return 0



T = int(input())

# 우 하 좌 상
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                startx, starty = i, j


    print(f"#{tc} {gogo(startx, starty, N)}")
    print()






