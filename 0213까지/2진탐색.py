

T = int(input())

for tc in range(1, T+1):
    total, A, B = map(int, input().split())

    l = 1 # 시작점
    r = total # 끝점
     # 중간점

    # A의 경우
    cnt_A = 0
    while l <= r:
        c = (l+r) // 2
        if c == A:
            cnt_A += 1
            break
        elif c > A:
            r = c
            cnt_A += 1
        else:
            l = c
            cnt_A += 1

    l = 1
    r = total
    cnt_B = 0
    while l <= r:
        c = (l+r) // 2
        if c == B:
            cnt_B += 1
            break
        elif c > B:
            r = c
            cnt_B += 1
        else:
            l = c
            cnt_B += 1

    if cnt_A < cnt_B:
        print(f"#{tc} A")
    elif cnt_A > cnt_B:
        print(f"#{tc} B")
    else:
        print(f"#{tc} 0")


