import sys
sys.stdin = open('input (9).txt', 'r')

T = 10

for tc in range(1, T+1):
    n = int(input())
    box = list(map(int, input().split()))

    # 최대 높이 박스 정보
    max_point = []
    # max_point[0] 최대상자탑의 위치
    # max_point[1] 최대상자탑의 높이

    # 최소 높이 박스 정보
    min_point = []
    # min_point[0] 최소상자탑의 위치
    # min_point[1] 최소상자탑의 높이

    while n > 0:
        max_point = [0, 0]
        min_point = [0, 100]

        # 반복문을 돌면서 전체 상자 높이를 확인하고 최대값과 최소값을 확인
        for i in range(100):
            if box[i] > max_point[1]:
                max_point = [i, box[i]]
            if box[i] < min_point[1]:
                min_point = [i, box[i]]


        # 최대 높이 -1 최저 높이 + 1

        box[max_point[0]] -= 1
        box[min_point[0]] += 1

        # 덤프 횟수 감소

        n -= 1
        max_height = 0
        min_height = 0
        # 다시 반복문을 돌리면서 최대, 최소값을 확인

        for i in range(100):
            if box[i] > max_height:
                max_height = box[i]
            if box[i] < min_height:
                min_height = box[i]

        print(f'#{tc} {max_height - min_height}')