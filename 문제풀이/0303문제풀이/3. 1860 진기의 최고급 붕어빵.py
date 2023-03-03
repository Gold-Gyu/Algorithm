import sys
sys.stdin = open("input (2).txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))   # 도착하는 사람들

    person = 0
    ans = "Possible"
    lst_a = sorted(lst)
    for t in lst_a:
        person += 1
        if person > (t//M) * K: #  도착한 사람수 > 만들어진 붕어빵
            ans = "Impossible"
            break
    print(f"#{tc} {ans}")

