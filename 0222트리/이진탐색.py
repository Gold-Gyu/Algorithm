import sys
sys.stdin = open('sample_input(1) (4).txt', 'r')


def inorder(v):
    global num  # num 은 1부터 차례대로 할당하고, 할당하면 1씩 증가
    # v번 노드가 존재하면 ( 트리 범위 안에 있다면 )
    if v <= n:
        # 왼쪽 자식에 할당 ( v * 2 )
        inorder(v * 2)
        # 자기 자신에 할당, num 1 증가
        tree[v] = num
        num += 1
        # 오른쪽 자식에 할당 ( v * 2 + 1)
        inorder(v * 2 + 1)


T = int(input())

for tc in range(1, T + 1):
    n = int(input())  # 이진탐색트리 노드의 개수

    tree = [0] * (n + 1)  # 만들어져 있음 (값은 나중에 할당)

    # 1부터 자리를 찾아가면서 순서대로 할당
    # 트리의 구조 : 작은수 < 중간 < 큰수
    # 1부터 점점 커지니까 중위 순회 방법을 사용해서 할당해보자
    num = 1
    inorder(1)
    print(tree)

    print(f"#{tc} {tree[1]} {tree[n // 2]}")


