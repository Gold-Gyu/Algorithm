import sys
sys.stdin = open('sample_input (1).txt', 'r')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))

    counts = [0] * (max(numbers) + 1)

    for i in numbers:
        counts[i] += 1

    # 리스트 중 최대값
    maxi = 0
    m = 0 #
    for i in range(len(counts)):
    # 인덱스를 통한 반복
    # i는 카드의 번호
    # maxi는 counts 요소들 중 최대값
    # m은 카드번호에서 최대값을 구하기 위한 변수
        if maxi < counts[i]:
            maxi = counts[i] # counts 중에서 가장 큰 값을 구한다
            m = i
        if maxi == counts[i]:
            if m < i:
                m = i

            # 카드 장수의 최대값과 내가 보고 있는 카드값이 같을 때

    print(counts)
    print(f'#{tc} {m} {maxi}')


