import sys
sys.stdin = open('sample_input (5).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 문자열 배열로 써도 되고
    # 문자열 그대로 서도 된다.
    lec = [list(input()) for _ in range(N)]
    print(lec)

    # 정답이 될 단어
    answer = ""

    # (0, 0)부터 문장을 만든 후에 뒤집어서 결과가 같은지 확인
    # j 범위 주의
    for i in range(N):
        for j in range(N-M+1):
            #(i,j) 부터 단어 만들기 시작
            # 가로, 세로 한번에
            word_row = ""
            word_col = ""
            # 우리가 원하는 단어의 길이는 : M
            # M만큼 문자를 뗴와서 문자열 만들기
            for k in range(M):
                word_row += lec[i][j + k]
                word_col += lec[j + k][i]
            print(word_row)

            # 뒤집은 뒤에 비교
            if word_row == word_row[::-1]:
                answer = word_row
            if word_col == word_col[::-1]:
                answer = word_col

    print(f"#{tc} {answer}")
