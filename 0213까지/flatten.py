import sys
sys.stdin = open('input (9).txt', 'r')

# 최대 위치와 높이 최소의 위치와 높이를 알 수 있느냐
# 인덱스가 중요.
for tc in range(1, 11):

    N = int(input())
    box = list(map(int, input().split()))


    for j in range(N + 1):

        # 최대값과 최소값을 구한다.

        max_num = 0
        min_num = 102
        for i in box:
            if max_num < i:
                max_num = i
            if min_num > i:
                min_num = i

        # 최대 최소의 인덱스 구하는 방법
        # max_index = 0
        # for k in range(len(box)):
        #     if box[k] == max_num:
        #         max_index = k
        #         print(k)

        box[box.index(max_num)] = box[box.index(max_num)] - 1
        box[box.index(min_num)] = box[box.index(min_num)] + 1


    print(f'#{tc} {max_num - min_num}')



