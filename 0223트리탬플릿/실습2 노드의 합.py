# 후위 순회

def postorder(i):
    # 트리의 범위
    if i > N:
        return 0
    else:
        if tree[i] != 0:
            return tree[i]
        else:
            left = postorder(i*2)
            right = postorder(i*2+1)
            tree[i] = left + right
            return tree[i]

# v = left + right
T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())

    tree = [0] * (N+1)
    for j in range(1, M+1):
        leafnum, nodenum = map(int, input().split())
        tree[leafnum] = nodenum


    print(f"#{tc} ", end = "")
    postorder(1)
    print(tree[L])