# 얉은 복사
# 람다 정렬
# 이차원 배열 전체 좌우대칭만들기
# 이차원 배열 다시 복습

r, c, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(3)]

ans = 0

# R 연산 == 행 정렬
def runR(arr, garo, sero):
    # 행을 하나 씩 꺼내서 정렬한다.
    maxV = 0
    newArr = []
    for i in range(garo): # 꺼내고
        numCheck = set()
        scope = [0] * 100
        newGaro = []
        garolst = []
        for j in range(sero):
            scope[arr[i][j]] += 1
            numCheck.add(arr[i][j])

        for cnt in numCheck:
            newGaro.append((cnt, scope[cnt]))
        newGaro = sorted(newGaro, key=lambda x: x[0])
        newGaro = sorted(newGaro, key= lambda x : x[1])

        for x in newGaro:
            garolst.append(x[0])
            garolst.append(x[1])
        if maxV < len(garolst):
            maxV = len(garolst)

        newArr.append(garolst)

    for x in range(len(arr)):
        arr.pop()

    for one in newArr:
        if len(one) <= maxV:
            for p in range(maxV - len(one)):
                one.append(0)
            arr.append(one)
# C 연산 == 열 정렬
def runC(arr, garo, sero):
    maxV = 0
    newArr = []
    for i in range(sero):  # 꺼내고
        numCheck = set()
        scope = [0] * 100
        newSero = []
        serolst = []

        for j in range(garo):
            if arr[j][i] == 0:
                continue
            scope[arr[j][i]] += 1
            numCheck.add(arr[j][i])

        for cnt in numCheck:
            newSero.append((cnt, scope[cnt]))
        newSero = sorted(newSero, key=lambda x: x[0])
        newSero = sorted(newSero, key=lambda x: x[1])

        for x in newSero:
            serolst.append(x[0])
            serolst.append(x[1])
        if maxV < len(serolst):
            maxV = len(serolst)
        newArr.append(serolst)

    for x in range(len(arr)):
        arr.pop()

    for one in newArr:
        if len(one) <= maxV:
            for p in range(maxV - len(one)):
                one.append(0)
            arr.append(one)

    arr = list(zip(*arr))
    print("C process", arr)


while True:
    if arr[r-1][c-1] == k:
        break
    if ans > 100:
        ans = -1
        break
    ans += 1
    garo = len(arr)
    sero = len(arr[0])

    if garo >= sero:
        runR(arr, garo, sero)
        print("R한 뒤", arr)
    else:
        runC(arr, garo, sero)
        print("C한 뒤", arr)
    # 종료 조건


print(ans)