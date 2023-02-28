def f(adjL, sp):
    visited = [0] * 101
    q = []
    q.append(sp)
    visited[sp] = 1
    maxV = 0
    while q:
        t = q.pop(0)
        for i in adjL[t]:
            if not visited[i]:
                visited[i] = visited[t] + 1
                q.append(i)
                if maxV < visited[i]:
                    maxV = visited[i]

    for i in range(101):
        if visited[i] == maxV:
            box.append(i)
    print(box)
    return max(box)


T = 10
for tc in range(1, T + 1):
    length, sp = map(int, input().split())
    lst = list(map(int, input().split()))
    box = []
    adjL = [[] for _ in range(101)]
    for i in range(length // 2):
        start, to = lst[i * 2], lst[i * 2 + 1]
        adjL[start].append(to)

    ans = f(adjL, sp)
    print(ans)
