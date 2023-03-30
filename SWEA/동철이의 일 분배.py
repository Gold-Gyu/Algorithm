"""
1
3
13 0 50
12 70 90
25 60 100

"""

T = int(input())


def f(i, selected, chance): # i가 행기(종업원), selected : 담당이 지정된 일(열), chance : 현재까지 확행
    # i = 0 selected [] chance 1
    # i = 1 selected =[0], chance = 0.13
    # i = 2 selected = [0, 1] chance = 0.13 * 0.7서 # 처음 i = 2
    # i = 3 selected = [0, 1, 2] chance = 0.13 * 0.7 * 1
    global maxV

    # 가지치
    if chance <= maxV:
        # 최대값보다 작은 확률은 확인 조차 하지 않는다.
        # 곱할 수록 작아지기 때문
        return

    if i == N: # 끝행에 왔따면( 모든 사람에게 일을 배정했다면)
        maxV = max(maxV, chance) # 확률의 최대값을 뽑는다서
        # 가면서 계산을 한다
        # 이게 무슨 말일까?
        return

    # i행에서 j열 뽑기
    for j in range(N):  # 일(열)을 고른다 0, 1, 2
        # i = 2 selected = [0, 1] chance = 0.13 * 0.7서 # 처음 i = 2
        if j not in selected:   # 순열에서 중복체크를 위해서 없으면
            selected.append(j)  # selected에 열(일) 넣는다. # 중복을 체크 = 순 위해서 넣는다.
            # i = 1 selected =[0, 2], chance = 0.13
            # i = 1 selected =[0, 1], chance = 0.13
            # i = 2 selected = [0, 1, 2] chance = 0.13 * 0.7서 # 처음 i = 2
            # i = 0 selected = [0] chance 1
            # i = 1 selected =[0, 2], chance = 0.13
            # why []만들어서 selected이름을 붙이고 함수의 인자까지 쳐넣어서 열을 쳐넣는냐??
            # selected = [0, 1, 2]

            f(i + 1, selected, chance * (field[i][j] / 100))    # 다음사람에게 일을 배정하러간다.
            # selected를 고대로 들고간다. 중복을 방지하기 위해
            # 다음 행에서 열을 다 골라보겠다.
            # selected 들고가는 이유?
            # 다음 행에서 열을 고를 떄 그전 행에서 골랐던 열은 고르면 안되기 때문에
            # f(2, selected, chance)
            # i = 1 selected =[0,1 ], chance = 0.13
            # i = 2 selected = [0, 1, 2] chance = 0.13 * 0.7
            # i = 1 selected =[0, 1], chance = 0.13
            # i = 2 selected = [0, 1, 2] chance = 0.13 * 0.7서 # 처음 i = 2
            selected.pop()  # 왜해주냐? 자리를 비워줘야 새로운 자리를 넣을 수 있다.
            # i = 2 selected = [0, 1] chance = 0.13 * 0.7 태빈이
            # i = 1 selected =[0], chance = 0.13 태빈
            # i = 2 selected = [0] chance = 0.13 * 0.7

for tc in range(1, T+1):
    N = int(input())    # 사람 수 이면서 일의 개수
    field = [list(map(int, input().split())) for _ in range(N)]

    # 최대값을 구한다
    maxV = 0
    f(0, [], 1)
    print(f'#{tc} {maxV * 100:.6f}')