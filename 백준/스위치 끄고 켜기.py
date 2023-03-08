T = int(input())

swich = list(map(int, input().split()))

N = int(input())    #학생
for tc in range(N):
    p, n = map(int, input().split())

    if p == 1:  # 남자라면
        for i in range(n-1, T, n):
            swich[i] = swich[i] * -1 + 1

    elif p == 2:    #여자라면
        left = n - 2
        right = n

        while True:
            if swich[left] == swich[right]:
                if left == 0 or right == T-1:
                    for i in range(left, right + 1):
                        swich[i] = swich[i] * -1 + 1    # 그 구간 전부다 반대로 바꿔주기
                    break
                elif left > 0 and right < T:
                    left -= 1
                    right += 1

            elif swich[left] != swich[right]:
                for i in range(left-1, right):
                    swich[i] = swich[i] * -1 + 1

for i in range(T):
    print(swich[i], end = " ")
    if i+1 % 20 == 0:
        print()





