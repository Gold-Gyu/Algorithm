# import sys
# sys.stdin = open("sample_input (1).txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())

    box = [0] * N

    for ans in range(1, Q+1):
        L, R = map(int, input().split())

        for i in range(L-1, R):
            box[i] = ans

    print(f"#{tc}", *box)