import sys
sys.stdin = open('sample_input (1).txt', 'r')

T = int(input())

for tc in range(1, T+1):
    n = int(input()) # 숫자 카드의 개수
    numbers = input()

    counts = [0] * 10

    # numbers에 있는 숫자 하나씩 보면서 개수 세기
    for num in numbers:
        counts[int(num)] += 1 # num 카드의 등장횟수 증가

    # 카드의 최대개수
    max_count = 0
    # 가장 큰 카드 번호(최대개수가 같은게 여러개일 경우) 0 ~ 9
    max_num = 0
    #counts[i]는 해당 번호 카드의 갯수
    for i in range(10):
        if counts[i] >= max_count:
            max_count = counts[i]
            max_num = i
    print(counts)
    print(f'#{tc} {max_num} {max_count}')
    # 또 다른 방법
    '''
        for i in range(10):
        if counts[i] > max_count:
            max_count = counts[i]
            max_num = i
        if counts[i] == max_count:
            # 카드 장수가 같은경우(최대값이 여러개임을 발견)
            if max_num < i:
                max_num = i
    
    '''