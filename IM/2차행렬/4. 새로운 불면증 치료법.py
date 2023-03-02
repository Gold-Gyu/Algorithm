import sys
sys.stdin = open("sample_input (18).txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = list(map(int, input()))

    num = 0
    for i in N:
        num += i
    print(num)




