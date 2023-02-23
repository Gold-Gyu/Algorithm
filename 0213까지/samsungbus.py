import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # N번 반복하면서 노선 입력, 빈도수 표시
    cnts = [0] *5001
    for i in range(N):
        S, E = map(int, input().split())
        for i in range(S, E + 1):
            cnts[i] += 1

    p = int(input())
    lst = []
    for j in range(1, p+1):
        lst.append(cnts[j])

    print(f'#{tc} {lst}')
