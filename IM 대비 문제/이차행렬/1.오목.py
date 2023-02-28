# for문으로 전체 탐색
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    ans = "NO"
    for i in range(N - 5 + 1):
        for j in range(N - 5 + 1):

            for k in range(5):
                cnt = 0
                for h in range(5):
                    if arr[i + k][j + h] == "o":
                        cnt += 1
                        if cnt == 5:
                            ans = "YES"

    for i in range(N - 5 + 1):
        for j in range(N - 5 + 1):

            for k in range(5):
                cnt2 = 0
                for h in range(5):
                    if arr[j + h][i + k] == "o":
                        cnt2 += 1
                        if cnt2 == 5:
                            ans = "YES"

    for i in range(N - 5 + 1):
        for j in range(N - 5 + 1):
            cnt3 = 0
            for k in range(5):
                if arr[i + k][j + k] == "o":
                    cnt3 += 1
                    if cnt3 == 5:
                        ans = "YES"
                else:
                    cnt = 0

    cnt4 = 0
    for i in range(N - 5 + 1):
        for j in range(N - 1, 3, -1):
            for k in range(5):
                if arr[i + k][j - k] == "o":
                    cnt4 += 1
                    if cnt4 == 5:
                        ans = "YES"
                else:
                    cnt4 = 0

    print(f"#{tc} {ans}")