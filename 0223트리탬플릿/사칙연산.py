import sys
sys.stdin = open('input (10).txt', 'r')


def mid(i):
    if i > T:
        return 0
    else:
        if tree[i] in ("*", "-", "+", "/"):
            left = mid(cleft[i])
            right = mid(cright[i])
            if tree[i] == "-":
                tree[i] = left - right
            elif tree[i] == "*":
                tree[i] = left * right
            elif tree[i] == "/":
                tree[i] = left // right
            elif tree[i] == "+":
                tree[i] = left + right
            return tree[i]
        else:
            return tree[i]


for tc in range(1, 11):
    T = int(input())
    cleft = [0] * (T + 1)
    cright = [0] * (T + 1)
    tree = [0] * (T + 1)

    for tc2 in range(1, T + 1):
        lst = input().split()
        p = int(lst[0])
        if lst[1].isdigit():
            tree[p] = int(lst[1])  # 트리 제작 완성
        else:
            tree[p] = lst[1]

        if len(lst) == 4:
            cleft[p] = int(lst[2])
            cright[p] = int(lst[3])  # 부모 노드를 인덱스로 리스트 생성 완료

    print(f"#{tc} ", end="")
    mid(1)
    print(tree[1])