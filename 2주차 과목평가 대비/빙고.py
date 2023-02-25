from pprint import pprint

def gogo():
#번호부른 횟수 세기
    count = 0
    for i in range(5):
        for j in range(5):
            cnt = arr2[i][j]    #  부르는 숫
            count += 1

            for k in range(5):
                for h in range(5):
                    if arr[k][h] == cnt:    # 부르는 숫자와 매칭되는 곳 0으로 바꿈
                        arr[k][h] = 0
                        break

            binggo = 0
            for a in range(5):
                cnt5 = 0
                for s in range(5):
                    if arr[a][s] == 0:
                        cnt5 += 1
                        if cnt5 == 5:
                            binggo += 1
                            if binggo == 3:
                                return count

            for u in range(5):
                cnt2 = 0
                for y in range(5):
                    if arr[y][u] == 0:
                        cnt2 += 1
                        if cnt2 == 5:
                            binggo += 1
                            if binggo == 3:
                                return count

            cnt3 = 0
            for l in range(5):
                if arr[l][l] == 0:
                    cnt3 += 1
                    if cnt3 == 5:
                        binggo += 1
                        if binggo == 3:
                            return count

            # 오른쪽에서 왼쪽 아래 대각선
            cnt4 = 0
            for f in range(4, -1, -1):
                if arr[4-f][f] == 0:
                    cnt4 += 1
                    if cnt4 == 5:
                        binggo += 1
                        if binggo >= 3:
                            return count
    return

arr = [list(map(int, input().split())) for _ in range(5)]
arr2 = [list(map(int, input().split())) for _ in range(5)]

# 숫자를 받으면 0 으로 바꾸기력
ans = gogo()
print(ans)
