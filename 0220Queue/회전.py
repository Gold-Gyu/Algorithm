import sys
sys.stdin = open('sample_input (3).txt', 'r')

# 5527, 731, 31274
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    # print(f"#{tc} {lst[M%N]}")
    n = len(lst)
    # 큐 만들기
    size = 1000
    q = [0] * size
    front = rear = -1
    for i in lst: # lst는 3이니까 rear은 총 3번 더해짐. -1 + 3 = 2
        rear += 1
        q[rear] = i
    print(q)

    # 현재 rear은 2, front는 1
    # 맨 앞의 숫자를 뒤로보내고 수열의 맨 앞에 있는 숫자를 출력하려면 front = 0에서 시작해야함.
    front = 0
    rear = n - 1
    for k in range(M):
        front += 1
        rear += 1
        q[rear] = q[k]  # k는 0 ~ 9
        if rear == front:
            print("공백상태")
        elif rear == n - 1:
            print("포화상태")
    print(f"#{tc} {q[front]}")
