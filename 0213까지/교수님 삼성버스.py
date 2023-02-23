import sys
sys.stdin = open('s_input.txt', 'r')
"""
1 => T
2 => n # 버스 노선 개수
1 3
2 5 => bus_list
5 => p
1
2
3
4
5

리스트를 범위화 하는 방법
"""
T = int(input())

for tc in range(1, T+1):
    n = int(input())

    bus_list = [list(map(int, input().split())) for _ in range(n)]# 각 노선 정보

    p = int(input()) # 정차 횟수 알고 싶은 정류장의 갯수
    stop = [int(input()) for _ in range(p)] # 정차 횟수 알고 싶은 정류장 번호
    cnt_stop = [0] * p # 각 정류장의 정차 횟수 ( 0부터 시작 )

    for i in range(n):
        for j in range(p):
            if bus_list[i][0] <= stop[j] <= bus_list[i][1]:
                cnt_stop[j] += 1
    # for i in range(n): # 2번 반복
    #     for j in range(p): # 5번 반복
    #         if stop[j] in range(bus_list[i][0], bus_list[i][1]+1):
    #             cnt_stop[j] += 1

        # 1 ~ 3까지 1씩 추가하고
        # 2 ~ 5까지 1씩 추가해라
    print(stop)

    print(f'#{tc}', *cnt_stop)


    # 버스 노선 개수만큼 반복하면서
    # stop의 갯수(p) 만큼 반복
    #   stop의 각 원소(정차 횟수 알고 싶은 정류장 번호)가 bus_list[i] 의 운행 정류장 범위에 포함되는지 검사
    #   만약 포함되면 cnt_stop[] += 1
