T = int(input())    # 입력값 받기
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]   # 배열 만들기

    treecount= 0   # 심은 나무의 수
    maxV = 0    # 가장 비싼 나무의 가격
    cnt = 0     # 총 나무 심은 비용
    for i in range(N):
        for j in range(0, M, 2):
            cnt += arr[j][i]
            treecount += 1  # 심은 나무의 수 + 1
            if maxV <= arr[j][i]:    # 모든 블록 당 가장 큰 수 = 가장 많은 나무의 수
                maxV = arr[j][i]
                col = j

    print(f"#{tc} {cnt} {treecount} {maxV} {col+1}")