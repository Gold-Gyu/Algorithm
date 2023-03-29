import sys
sys.stdin = open("이진탐색.txt", "r")


T = int(input())

R = 1
L = 0

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split()))) # 정렬
    B = list(map(int, input().split()))

    # 조건에 맞으면서 A안에 있는 B의 원소의 개수를 찾는다

    cnt = 0
    # 조건은?
    # 이진탐색할 때 왼쪽 / 오른쪽 번갈아가며 찾는 원소의 개수
    # 이전에 내가 왼쪽을 선택했다면, 다음에 또 왼쪽 선택 x
    for number in B:
        left = 0
        right = N - 1
        dir = -1 # 처음 찾기 시작할 떄는 방향이 없다.
        # 방향이 같으면 종료

        while left <= right:
            mid = (left + right) // 2

            # 답을 찾았으면 개수 증가
            if A[mid] == number:
                cnt += 1
                break

            # 답을 못찾으면
            # 내가 찾는게 mid보다 작으면 왼쪽
            elif A[mid] > number:
                right = mid - 1
                if dir == L:
                    break
                dir = L

                # 내가 선택한 방향은 왼쪽
                # 내가 이전에 선택했던 방향도 왼쪽이면 종료

            # 내가 찾는게 mid보다 오른쪽
            else:
                left = mid + 1
                # 내가 선택한 방향이 오른쪽일 때
                # 이전에 내가 선택했던 방향이 오른쪽이면 안됨
                if dir == R:
                    break
                dir = R
    print(f"#{tc} {cnt}")