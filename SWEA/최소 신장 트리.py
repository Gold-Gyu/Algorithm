import sys
sys.stdin = open("최소 신장 트리.txt", "r")

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    for _ in range(E):
        v1, v2, w = map(int, input().split())
        print(v1, v2, w)
    print("=====")