n, k = map(int, input().split())
arr = list(map(int, input().split()))
size = len(arr)

robot = [0] * n
ans = 0
cnt = 0
# 1 단계 컨베이어 벨트 이동 + 로봇과 함께

# 이동
# n-1 은 2n-1 자리로
# n 자리는 0자리로
while True:
    ans += 1
    # 1 벨트, 로봇 회전 + [n-1]자리에서 로봇 내림

    # 방법 1. 인덱싱
    # arr = [arr[-1]] + arr[:-1]
    # robot = [0] + robot[:-1]
    # robot[n-1] = 0 # 로봇 내림

    # 방법 2. pop과 insert을 통한 방법
    arr.insert(0, arr.pop())
    robot.pop()
    robot.insert(0, 0)
    robot[n-1] = 0


    # 2 먼저 올라간 로봇부터 처리
    for i in range(n-2, 0, -1):
        if robot[i] == 1 and robot[i+1] == 0 and arr[i+1] > 0:
            robot[i], robot[i+1] = 0, 1
            arr[i+1] -= 1   # 내구도 감소
            if arr[i+1] == 0:
                cnt += 1

    # 3 [0] 번째 자리 내구도가 > 0이면 로봇 올린다.
    if arr[0] > 0:
        robot[0] = 1
        arr[0] -= 1
        if arr[0] == 0:
            cnt += 1

    # 4 arr 원소 중 0의 개수가 k개이면 종료
    if cnt >= k:
        break

print(ans)