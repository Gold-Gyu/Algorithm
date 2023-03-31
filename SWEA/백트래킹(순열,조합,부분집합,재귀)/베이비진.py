import sys
sys.stdin = open("베이비진.txt", 'r')

T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    # 첫 번째 사람이 받는 카드
    person1 = []
    # 첫 번째 사람의 카운트배열
    counting1 = [0] * 10
    # 두 번째 사람이 받는 카드
    person2 = []
    # 두 번째 사람의 카운트배열
    counting2 = [0] * 10
    # 이긴 사람
    winner = 0

    # 반복문 빠져나오기
    flag1 = 0   # 짝수 번째
    flag2 = 0   # 홀수 번째
    count = 0
    count2 = 0
    for i in range(len(lst)):
        # 하나씩 들어올 때마다 체크해보기

        if (i+1) % 2 == 0:  # 짝수면
            counting2[lst[i]] += 1  # 카운팅배열 체크
            person2.append(lst[i])  # 리스트에 넣기

            # triplet 확인
            for num in range(len(counting2)):   # 하나씩 돌려가며
                if counting2[num] == 3:    # 같은 숫자가 3인 경우 trip
                    winner = 2
                    flag1 = 1
                    break   # for num
                if num >= 0:
                    if counting2[num]:
                        count += 1
                        if count == 3:
                            winner = 2
                            flag1 = 1
                            break
                    else:
                        count = 0
            if flag1:
                break   # for i

            # run 확인
            p2 = sorted(person2)
            if len(p2) >= 3:
                count = 0
                for j in range(1, len(p2)):
                    if p2[j] - p2[j-1] == 1:
                        count += 1
                        if count == 2:
                            winner = 2
                            flag1 = 1
                            break # for j
                    else:
                        count = 0
                if flag1:
                    break # for num

        else:
            counting1[lst[i]] += 1
            person1.append(lst[i])

            # triplet 확인
            for num in range(len(counting1)):  # 하나씩 돌려가며
                if counting1[num] == 3:  # 같은 숫자가 3인 경우 trip
                    winner = 1
                    flag2 = 1
                    break  # for num
                if num >= 0:
                    if counting1[num]:
                        count2 += 1
                        if count2 == 3:
                            winner = 1
                            flag2 = 1
                            break
                    else:
                        count2 = 0

            if flag2:
                break  # for i

            # run 확인
            p1 = sorted(person1)
            if len(p1) >= 3:
                count2 = 0
                for j in range(1, len(p1)):
                    if p1[j] - p1[j - 1] == 1:
                        count2 += 1
                        if count2 == 2:
                            winner = 1
                            flag2 = 1
                            break
                    else:
                        count2 = 0
                if flag2:
                    break

    # print(p1)
    # print(counting1)
    # print(p2)
    # print(counting2)
    print(f"#{tc} {winner}")

