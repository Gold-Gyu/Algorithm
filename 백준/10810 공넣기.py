N, M = map(int, input().split())

box = [0] * (N)
for _ in range(1, M+1):
    i, j, k = map(int, input().split())

    for g in range(i-1, j):
        box[g] = k

print(*box)