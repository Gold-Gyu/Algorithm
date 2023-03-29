import sys
sys.stdin = open("이진탐색.txt", "r")


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lstB = sorted(list(map(int, input().split())))
    lstA = sorted(list(map(int, input().split())))
    # 시작 l
    # 끝은 r
    count = 0   # 조건에 부합하고 이진탐색으로 찾은 수의 개수

    for key in lstA: # 하나씩 꺼내서
        cnt = 0  # 왼쪽으로 이동할 떄
        cnt2 = 0  # 오른쪽으로 이동할 때
        if key in lstB: # 리스트 안에 있으면
            left = 0    # left를 0으로
            right = len(lstB) - 1   # right를 M-1로

            while left <= right:    # 교차할때까지 반복

                mid = (left + right) // 2   # 미드값

                if lstB[mid] == key:    # 같다면
                    if (cnt == 1 and cnt2 == 1) or (cnt == 0 and cnt2 == 0) or (cnt == 1 or cnt2 == 1):    # 왼쪽, 오른쪽으로 가봤거나, 아니면 바로 키값이면
                        count += 1
                        break

                elif lstB[mid] > key:   # 왼쪽으로 이동
                    right = mid - 1 # 오른쪽 범위를 mid - 1로 조정
                    cnt += 1
                    if cnt == 2 and cnt2 == 0:    # 왼쪽으로 이동 2번이상이면 그냥 바로 while문 종료
                        break   # while

                else:
                    left = mid + 1
                    cnt2 += 1
                    if cnt2 == 2 and cnt == 0:
                        break   # while

    print(f'#{tc} {count}')