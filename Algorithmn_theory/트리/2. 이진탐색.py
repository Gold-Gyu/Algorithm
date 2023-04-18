import sys
sys.stdin = open('sample_input(1) (3).txt', 'r')

def gogo(i):
    global num
    if i <= N:
        gogo(i*2)
        tree[i] = num
        num += 1
        gogo(i*2+1)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)

    num = 1
    gogo(1)

    print(f"#{tc} {tree[1]} {tree[N//2]}")