import sys

sys.stdin = open('input1.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))
    cnt = 0
    ans = 0

    for num in numbers:
        if num == 1:
            cnt += 1
            if cnt > ans:
                ans = cnt
        else:
            cnt = 0

    print(f'#{tc} {ans}')

