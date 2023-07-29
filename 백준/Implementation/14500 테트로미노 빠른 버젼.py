N, M = map(int, input().split())
array = []

for i in range(N):
    array.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    for j in range(M):
        if j + 3 < M:  # ㅡ
            ans = max(sum(array[i][j:j + 4]), ans)

        if i + 3 < N:
            ans = max(array[i][j] + array[i + 1][j] + array[i + 2][j] + array[i + 3][j], ans)

        if j + 2 < M and i + 1 < N:  # ㅜ
            ans = max(sum(array[i][j:j + 3]) + array[i + 1][j + 1], ans)
            ans = max(sum(array[i][j:j + 2]) + sum(array[i + 1][j + 1:j + 3]), ans)
            ans = max(array[i][j] + sum(array[i + 1][j:j + 3]), ans)
            ans = max(sum(array[i][j:j + 3]) + array[i + 1][j], ans)
            ans = max(sum(array[i][j:j + 3]) + array[i + 1][j + 2], ans)

        if j + 1 < M and i + 2 < N:  # L
            ans = max(array[i][j] + array[i + 1][j] + array[i + 2][j] + array[i + 2][j + 1], ans)
            ans = max(array[i][j] + sum(array[i + 1][j:j + 2]) + array[i + 2][j + 1], ans)
            ans = max(array[i][j] + array[i][j + 1] + array[i + 1][j + 1] + array[i + 2][j + 1], ans)
            ans = max(array[i][j] + array[i + 1][j] + array[i + 2][j] + array[i + 2][j + 1], ans)
            ans = max(array[i][j] + array[i][j + 1] + array[i + 1][j] + array[i + 2][j], ans)
            ans = max(array[i][j] + array[i + 1][j] + array[i + 1][j + 1] + array[i + 2][j], ans)

        if j + 1 < M and i + 1 < N:  # ㅁ
            ans = max(sum(array[i][j:j + 2]) + sum(array[i + 1][j:j + 2]), ans)

        if j - 1 >= 0 and i + 2 < N:
            ans = max(array[i][j] + array[i + 1][j] + array[i + 1][j - 1] + array[i + 2][j - 1], ans)
            ans = max(array[i][j] + array[i + 1][j] + array[i + 2][j] + array[i + 1][j - 1], ans)
            ans = max(array[i][j] + array[i + 1][j] + array[i + 2][j] + array[i + 2][j - 1], ans)

        if i - 1 >= 0 and j + 2 < M:
            ans = max(sum(array[i][j:j + 3]) + array[i - 1][j + 1], ans)
            ans = max(sum(array[i][j:j + 2]) + sum(array[i - 1][j + 1:j + 3]), ans)
            ans = max(sum(array[i][j:j + 3]) + array[i - 1][j + 2], ans)

print(ans)