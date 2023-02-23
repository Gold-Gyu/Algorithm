import sys
sys.stdin = open('input (10).txt', 'r')

# 하위
def mid(i):
    global ans
    if i > T:
        return 0
    else:
        if tree[i]:
            return tree[i]
        else:
            left = mid(i * 2)
            right = mid(i * 2 + 1)
            if tree[i] == "-":
                ans = left - right
            elif tree[i] == "*":
                ans = left * right
            elif tree[i] == "/":
                ans = left // right
            elif tree[i] == "+":
                ans = left + right
            return ans


for tc in range(1, 11):
    T = int(input())
    cleft = [0] * (T + 1)
    cright = [0] * (T + 1)
    tree = [0] * (T + 1)
    ans = 0
    for tc2 in range(1, T+1):
        lst = input().split()
        p = int(lst[0])
        if lst[1].isdigit():
            tree[p] = int(lst[1])        # 트리 제작 완성
        else:
            tree[p] = lst[1]

        if len(lst) == 4:
            cleft[p] = int(lst[2])
            cright[p] = int(lst[3])      # 부모 노드를 인덱스로 리스트 생성 완료

    print(tree)
    print(cleft)
    print(cright)

    print(f"#{tc} ", end="")
    mid(1)
    print()
