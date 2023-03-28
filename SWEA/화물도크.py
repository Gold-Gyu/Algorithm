import sys
sys.stdin = open('화물도크.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = []
    for _ in range(N):
        s, e = map(int, input().split())
        lst.append((s, e))

    ans = sorted(lst, key=lambda a: a[0])
    ans = sorted(lst, key=lambda a: a[1])

    last = count = 0
    for i, j in ans:
        if i >= last:
            count += 1
            last = j
    print(f"#{tc} {count}")