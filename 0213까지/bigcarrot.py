import sys

sys.stdin = open('input (10).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))


    cnt = 0

    for i in range(N+1):
        if numbers[i] + 1 < numbers[i+1]:
            cnt += 1






# print(f'#{tc} {}')

