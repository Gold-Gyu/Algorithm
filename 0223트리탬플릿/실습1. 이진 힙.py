def enq(item):
    # 삽입을 했다면 마지막 위치를 수정해야함.
    global last
    last += 1   # 마지막 위치에 원소 추가
    heap[last] = item

    # 추가를 하고 나서 부모 노드가 자식 노드보다 크다는 조건을 만족해야한다.
    c = last    # 현재 위치를 자식으로 생각
    p = c // 2  # 부모의 위치 찾기

    # 부모 노드가 존재하고, 자식이 부모보다 작을 때까지 위치를 바꿔준다.
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 자리를 바꿨으면
        # 자식의 위치를 다시 바꾸고 계속 진행
        c = p   # 자리를 바꿨으니 자식이 이제 부모가 됨
        p = c // 2

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    heap = [0] * 501
    # 마지막에 넣은 원소의 위치
    last = 0
    for i in nums:
        item = i
        enq(item)
    cnt = 0
    while N:
        N = N // 2
        cnt += heap[N]
    print(f'#{tc} {cnt}')

