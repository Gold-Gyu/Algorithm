
T = int(input())

for tc in range(1, T+1):
    clap = list(map(int, input()))
    n = len(clap)
    cnt = 0

    for i in range(n-1):
        if clap[i] == 0:
            if sum(clap[:i]) <= i and sum(clap[:i+1]) < i+1:
                clap[i] = 1
                cnt += 1

    print(f"#{tc} {cnt}")
