import sys
sys.stdin = open('input (9).txt', 'r')
# 이진트리가 아닐 경우 왼쪽자식과 오른쪽자식 정보를  부모노드기반 인덱스 리스트로 받아서 작성해보기

def f(i):
    if i > 0:  # 유효한 정점 i  # 0이면 실존하지 않는 정점이
        f(left[i])  # i의 왼쪽 자식으로 이동
        print(data[i], end="")
        f(right[i])  # i의 오른쪽 자식으로 이동
    return


T = 10
for tc in range(1, T + 1):
    n = int(input())
    left = [0] * (n + 1)  # 왼쪽자식노드
    right = [0] * (n + 1)  # 오른쪽 자식 노드
    data = [0] * (n + 1)  # 각 노드가 가진 글자 정보 저장

    for _ in range(n):
        arr = list(input().split())
        p = int(arr[0])  # 노드 번호    # 부모노드 인덱스
        alpa = arr[1]
        data[p] = alpa
        if len(arr) == 4:  # 4글자
            left[p] = int(arr[2])
            right[p] = int(arr[3])
        elif len(arr) == 3:  # 3글자
            left[p] = int(arr[2])

    print(f"#{tc} ", end="")
    f(1)
    print()