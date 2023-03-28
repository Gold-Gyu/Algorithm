import sys
sys.stdin = open('컨테이너운반.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())


    # 컨테이너
    w = list(map(int, input().split()))
    # 트럭
    t = list(map(int, input().split()))

    # greedy ?? 큰 컨테이너부터 옮기자 ==> 큰 트럭부터 선택
    # 정렬을 통해서

    # 내림차순으로 정렬하면 첫번째 원소가 가장 크게 된다. => 0부터 시작 가능
    weight = sorted(w, reverse=True)
    total = sorted(t, reverse=True)

    # 다음에 이동할 컨테이너, 트럭의 인덱스
    wi = 0
    ti = 0

    # 옮긴 화물의 총 중량
    moved = 0

    # 트럭을 보낼 수 있을 때 까지
    while wi < N and ti < M:
        # 현재 옮길 차례의 화물이 트럭에 실을 수 있다면 총 중량 증가
        if weight[wi] < total[ti]:
            moved += weight[wi]
            wi += 1
            ti += 1
        # 트럭이 작아서 wi 번째 화물을 못 옮길 경우
        else:
            wi += 1

    print(f"#{tc} {moved}")