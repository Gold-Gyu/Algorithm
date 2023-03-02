N, M = map(int, input().split())
words = [list(input()) for _ in range(N)]

ans = []

for i in range(N):
    row_word = ""
    for j in range(M):
        if words[i][j] != "#":
            row_word += words[i][j]
        else:
            if len(row_word) > 1:
                ans.append(row_word)
                row_word = ""
            else:
                row_word = ""
    if len(row_word) > 1:
        ans.append(row_word)

for i in range(M):
    col_word = ""
    for j in range(N):
        if words[j][i] != "#":
            col_word += words[j][i]
        else:
            if len(col_word) > 1:
                ans.append(col_word)
            else:
                col_word = ""
    if len(col_word) > 1:
        ans.append(col_word)

length = len(ans)
for i in range(length-1):
    min_ = i
    for j in range(i, length):
        if ans[j] < ans[min_]:
            min_ = j
    ans[i], ans[min_] = ans[min_], ans[i]

print(ans[0])