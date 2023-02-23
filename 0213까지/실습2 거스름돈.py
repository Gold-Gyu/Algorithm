T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 거스름돈

    # 화폐종류 = 8가지
    counts = [0] * 8

    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    # 5만원권부터 시작
    # 현재 남은 거스름돈에서 50000을 뺀다
    # 현재 남은 거스름돈이 50000보다 작아질 때까지 # while
    # 뺄 때 마다 5만원권 사용 갯수를 1 증가시켜주면 된다.

    # 화폐 종류 8가지에 대해서 거스름돈 걸러주기 반복
    for i in range(len(money)):
        # 남은 거스름돈 n이 지금 화폐단위 money[i] 이상이라면 거스름돈으로 현재 화폐 사용 가능
        # 현재 화폐 가치만 거스름돈 빼주고 사용횟수 증가가
       while N >= money[i]:
            N = N - money[i]
            counts[i] += 1



    # while N >= 50000:
    #     N = N - 50000
    #     counts[0] += 1
    #
    # while N >= 10000:
    #     N = N - 10000
    #     counts[1] += 1
    #
    # while N >= 5000:
    #     N = N - 5000
    #     counts[2] += 1
    #
    # while N >= 1000:
    #     N = N - 1000
    #     counts[3] += 1
    #
    # while N >= 500:
    #     N = N - 500
    #     counts[4] += 1
    #
    # while N >= 100:
    #     N = N - 100
    #     counts[5] += 1
    #
    # while N >= 50:
    #     N = N - 50
    #     counts[6] += 1
    #
    # while N >= 10:
    #     N = N - 10
    #     counts[7] += 1
    #
    counts2 = ' '.join(map(str,counts))

    print(f'#{tc}\n{counts2}')
