import sys
sys.stdin = open('sample_input (5).txt', 'r')

# 왼쪽을 다 확인한 후에 오른쪽을 확인한다/


def preorder(t):    # 노드가 1일 때
    global cnt
    if t:       # t = 1일 떄 t가 있으면... 1이 잇다...? ㅇ?
        cnt += 1

        preorder(child_left[t])
        preorder(child_right[t])
    return cnt

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = list(map(int, input().split()))

    # 부모 노드로 인덱스 형성
    child_left = [0] * (E+2)
    child_right = [0] * (E+2)

    for i in range(E):
        parents = tree[i * 2]
        child = tree[i * 2 + 1]
        if child_left[parents] == 0:
            child_left[parents] = child
        else:
            child_right[parents] = child

    cnt = 0
    ans = preorder(N)
    print(f"#{tc} {ans}")

