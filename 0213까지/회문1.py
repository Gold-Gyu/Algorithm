import sys
sys.stdin = open('input (12).txt', 'r')



for tc in range(1, 11):
    T = int(input())
    arr = [list(input()) for _ in range(8)]

    cnt = 0
    for i in range(8):
        for j in range(8 - T + 1):
            word_row = ""
            word_col = ""
            for k in range(T):
                word_row += arr[i][j+k]
                word_col += arr[j+k][i]
            if word_row == word_row[::-1]:
                cnt += 1
            if word_col == word_col[::-1]:
                cnt += 1

    print(f"#{tc} {cnt}")
