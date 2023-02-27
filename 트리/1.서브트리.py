import sys
sys.stdin = open('sample_input (15).txt', 'r')


def gogo(N):
    global count
    if N:
        count += 1
        gogo(cleft[N])
        gogo(cright[N])
    return count
T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))
    cleft = [0] * (E+2)
    cright = [0] * (E+2)
    count = 0
    for i in range(E):
        p, c = nodes[i*2], nodes[i*2+1]

        if cleft[p] == 0:
            cleft[p] = c
        else:
            cright[p] = c

    ans = gogo(N)
    print(f"#{tc} { ans}")

