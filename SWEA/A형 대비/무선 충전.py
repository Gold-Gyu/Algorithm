import sys
sys.stdin = open("무선충전.txt", "r")

from collections import deque
from pprint import pprint

def go_a(step):
    global x1
    global y1
    nx = x1 + dx[move_A[step]]
    ny = y1 + dy[move_A[step]]
    if 0 <= nx < 10 and 0 <= ny < 10:
        x1 = nx
        y1 = ny
        visited[x1][y1] = 1
def go_b(step):
    global x2
    global y2
    nx = x2 + dx[move_B[step]]
    ny = y2 + dy[move_B[step]]
    if 0 <= nx < 10 and 0 <= ny < 10:
        x2 = nx
        y2 = ny
        visited[x2][y2] = 1
def makeBC(r, c, time):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    v = [[0] * 10 for _ in range(10)]
    q = deque()
    q.append((r, c))
    v[r][c] = 1
    arr[r][c] = num

    for x in range(time):
        for x in range(len(q)):
            r, c = q.popleft()
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < 10 and 0 <= nc < 10 and v[nr][nc] == 0:
                    if arr[nr][nc]:
                        q.append((nr, nc))
                        arr[nr][nc] = [arr[nr][nc], num]
                        v[nr][nc] = 1
                    else:
                        q.append((nr, nc))
                        arr[nr][nc] = num
                        v[nr][nc] = 1

T = int(input())
arr = [[0] * 10 for _ in range(10)]
visited = [[0] * 10 for _ in range(10)]
dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]


for tc in range(1, T+1):
    cnt1 = 0
    cnt2 = 0
    pointlst = [0]
    m, point = map(int, input().split())
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))

    for num in range(1, point+1):
        x, y, c, p = map(int, input().split())
        makeBC(x-1, y-1, c)
        pointlst.append(p)
    pprint(arr)
    if arr[0][0] == 0:
        cnt1 += 0
        visited[0][0] = 1
    if arr[9][9] == 0:
        cnt2 += 0
        visited[9][9] = 1
    else:
        for c in range(1, point):
            # A의 시작점
            visited[0][0] = 1
            if arr[0][0] == c:
                cnt1 += pointlst[c]
                break
            elif type(arr[0][0]) == list:
                maxV = 0
                for i in arr[0][0]:
                    if maxV < pointlst[i]:
                        maxV = pointlst[i]
                cnt1 += maxV
                break
        for c in range(1, point):
            visited[9][9] = 1
            if arr[9][9] == c:
                cnt2 += pointlst[c]
                break
            elif type(arr[9][9]) == list:
                maxV2 = 0
                for p in arr[9][9]:
                    if maxV2 < pointlst[p]:
                        maxV2 = pointlst[p]
                cnt2 += maxV2
                break
    # 이동하기
    x1, y1 = 0, 0
    x2, y2 = 9, 9
    for step in range(m):

        go_a(step)
        go_b(step)

        # 두개 다 리스트인 경우
        if type(arr[x1][y1]) == list and type(arr[x2][y2]) == list:
            checklst =[1] + [0] * 10
            print(checklst)
            maxV3 = 0
            for i in arr[x1][y1]:
                if maxV3 < pointlst[i] and checklst[i] == 0:
                    maxV3 = pointlst[i]
                    z = i
            checklst[z] = 1
            cnt1 += maxV3
            maxV5 = 0
            for j in arr[x1][y1]:
                if maxV5 < pointlst[j] and checklst[j] == 0:
                    maxV5 = pointlst[j]
                    p = j
            checklst[p] = 1
            cnt2 += maxV5
        # 하나만 리스트인 경우
        elif type(arr[x1][y1]) != list and type(arr[x2][y2]) == list:
            maxV4 = 0
            checklst = [1] + [0] * 10
            print(checklst)
            cnt1 += pointlst[arr[x1][y1]]
            checklst[arr[x1][y1]] = 1
            for i in arr[x2][y2]:
                print(i)
                if maxV4 < pointlst[i] and checklst[i] == 0:
                    maxV4 = pointlst[i]
            cnt2 += maxV4

        elif type(arr[x1][y1]) == list and type(arr[x2][y2]) != list:
            maxV7 = 0
            for i in arr[x1][y1]:
                if maxV7 < pointlst[i]:
                    maxV7 = pointlst[i]
            cnt1 += maxV7
            cnt2 += pointlst[arr[x2][y2]]

        # 둘다 리스트도 아닌데 같은 위치에 있는 경
        elif arr[x1][y1] == arr[x2][y2] and arr[x1][y1] and arr[x2][y2]:
            ans = arr[x1][y1]
            cnt1 += pointlst[ans] // 2
            cnt2 += pointlst[ans] // 2
            # 둘다 리스트가 아닌 경우
        else:
            cnt1 += pointlst[arr[x1][y1]]
            cnt2 += pointlst[arr[x2][y2]]
    print(f"#{tc} {cnt1+cnt2}")