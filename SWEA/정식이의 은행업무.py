import sys
sys.stdin = open('정식이의 은행업무.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    two = list(map(int, input()))
    two_num = len(two)

    three = list(map(int, input()))
    three_num = len(three)


    # 하나의 금액을
    # 2진수와 3진수 형태로 기억
    real_mean_two = 0
    sum_ = 0
    # 2진수 로직
    for i in two:
        two_num -= 1
        print(two_num)
        real_mean_two += i * (2 ** two_num)
    


    # 3진수 로직


    # 모든 경우의 수를 돌려가며 숫자 하나씩 고쳤을 때 같아지는 것 = > 내가 원하는 값


    # print(f"#{tc} ")